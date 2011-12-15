#!/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         anag/clifor_datifisc.py
# Author:       Fabio Cassini <fabio.cassini@gmail.com>
# Copyright:    (C) 2011 Astra S.r.l. C.so Cavallotti, 122 18038 Sanremo (IM)
# ------------------------------------------------------------------------------
# This file is part of X4GA
# 
# X4GA is free software: you can redistribute it and/or modify
# it under the terms of the Affero GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# X4GA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with X4GA.  If not, see <http://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------------

import wx

import awc.controls.windows as aw
import awc.controls.dbgrid as dbgrid

import anag.pdcrel_wdr as wdr

import stormdb as adb

import Env
bt = Env.Azienda.BaseTab

from anag.clienti import ClientiDialog
from anag.fornit import FornitDialog

from awc.lib import ControllaPIVA, ControllaCodFisc

import report as rpt


FRAME_TITLE = "Dati fiscali"


class _CliFor_DatiFiscaliGrid(dbgrid.ADB_Grid):
    
    _AnagClass = None
    
    def __init__(self, parent, dbana):
        
        self.dbana = anag = dbana
        pdc = anag.pdc
        
        dbgrid.ADB_Grid.__init__(self, parent, db_table=dbana, can_edit=True, on_menu_select='row')
        
        AC = self.AddColumn
        AC(pdc,  'descriz', label='Descrizione', col_width=300, is_fittable=True)
        AC(anag, 'nazione', label='Stato', col_width=60)
        AC(anag, 'piva', label='P.IVA', col_width=100, is_editable=True)
        AC(anag, 'codfisc', label='Cod.Fiscale', col_width=140, is_editable=True)
        AC(anag, 'allegcf', label='All.', col_width=50, col_type=self.TypeCheck())
        AC(anag, 'aziper', label='A/P', col_width=50, is_editable=True)
        
        self.CreateGrid()
        
    def ShowContextMenu(self, position, row, col):
        
        self.ResetContextMenu()
        
        def ApriScheda(event):
            anag = self.dbana
            anag.MoveRow(row)
            dlg = self._AnagClass(None, onecodeonly=anag.id)
            dlg.OneCardOnly(anag.id)
            dlg.CenterOnScreen()
            dlg.ShowModal()
            dlg.Destroy()
            anag.Retrieve()
            self.ChangeData(anag.GetRecordset())
        
        self.AppendContextMenuVoice('Apri scheda anagrafica', ApriScheda)
        
        return dbgrid.ADB_Grid.ShowContextMenu(self, position, row, col)
    
    def CellEditBeforeUpdate(self, row, gridcol, col, value):
        
        anag = self.dbana
        anag.MoveRow(row)
        
        def cc(tab, colname):
            return tab._GetFieldIndex(colname, inline=True)
        
        if col == cc(anag, 'aziper'):
            valid = (value in 'AP')
            if not valid:
                aw.awu.MsgDialog(self, 'Valori contentiti: A, P', style=wx.ICON_ERROR)
            return valid
        
        elif col == cc(anag, 'piva') and len(value)>0:
            ctr = ControllaPIVA()
            ctr.SetPIva(value, anag.nazione or "IT")
            valid = ctr.Controlla()
            if not valid:
                aw.awu.MsgDialog(self, ctr.GetStatus(), style=wx.ICON_ERROR)
            return valid
        
        elif col == cc(anag, 'codfisc') and len(value)>0:
            ctr = ControllaCodFisc()
            ctr.SetCodFisc(value)
            valid = ctr.Controlla()
            if not valid:
                aw.awu.MsgDialog(self, ctr.GetStatus(), style=wx.ICON_ERROR)
            return valid
        
        return True


# -----------------------------------------------------------------------------


class _CliFor_DatiFiscaliPanel(aw.Panel):
    
    _GridClass = None
    tabanag = None
    
    def __init__(self, *args, **kwargs):
        
        aw.Panel.__init__(self, *args, **kwargs)
        wdr.CliFor_DatiFiscaliFunc(self)
        cn = self.FindWindowByName
        
        self.dbana = adb.DbTable(self.tabanag, 'anag')
        self.dbana.AddJoin(bt.TABNAME_PDC, 'pdc', idLeft='id')
        self.dbana.AddOrder('pdc.descriz')
        self.dbana.Retrieve()
        
        self.gridpdc = self._GridClass(cn('pangridpdc'), self.dbana)
        
        self.Bind(wx.EVT_BUTTON, self.OnSaveData)
    
    def OnSaveData(self, event):
        anag = self.dbana
        if anag.Save():
            aw.awu.MsgDialog(self, 'I dati sono stati correttamente salvati', style=wx.ICON_INFORMATION)
            event.Skip()
        else:
            aw.awu.MsgDialog(self, repr(anag.GetError()), style=wx.ICON_ERROR)


# ------------------------------------------------------------------------------


class Clienti_DatiFiscaliGrid(_CliFor_DatiFiscaliGrid):
    _AnagClass = ClientiDialog

class Clienti_DatiFiscaliPanel(_CliFor_DatiFiscaliPanel):
    _GridClass = Clienti_DatiFiscaliGrid
    tabanag = bt.TABNAME_CLIENTI

class Clienti_DatiFiscaliFrame(aw.Frame):
    
    def __init__(self, *args, **kwargs):
        if not 'title' in kwargs:
            kwargs['title'] = '%s %s' % (FRAME_TITLE, 'clienti')
        aw.Frame.__init__(self, *args, **kwargs)
        self.AddSizedPanel(Clienti_DatiFiscaliPanel(self))


# ------------------------------------------------------------------------------


class Fornitori_DatiFiscaliGrid(_CliFor_DatiFiscaliGrid):
    _AnagClass = FornitDialog

class Fornitori_DatiFiscaliPanel(_CliFor_DatiFiscaliPanel):
    _GridClass = Fornitori_DatiFiscaliGrid
    tabanag = bt.TABNAME_FORNIT

class Fornitori_DatiFiscaliFrame(aw.Frame):
    
    def __init__(self, *args, **kwargs):
        if not 'title' in kwargs:
            kwargs['title'] = '%s %s' % (FRAME_TITLE, 'fornitori')
        aw.Frame.__init__(self, *args, **kwargs)
        self.AddSizedPanel(Fornitori_DatiFiscaliPanel(self))
