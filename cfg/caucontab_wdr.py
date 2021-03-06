# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: caucontab.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
from anag.basetab import AnagCardPanel

from awc.controls.textctrl import TextCtrl
from awc.controls.numctrl import NumCtrl
from awc.controls.datectrl import DateCtrl
from awc.controls.radiobox import RadioBox
from awc.controls.checkbox import CheckBox
from awc.controls.linktable import LinkTable
from awc.controls.dbgrid import DbGrid

from anag.basetab import WorkZoneNotebook

from anag.pdctip import PdcTipDialog
from cfg.regiva import RegIvaDialog
from cfg.eventi import TipiEventoDialog

from cfg.pdcpref import PdcPrefCauPanel

from Env import Azienda
bt = Azienda.BaseTab


class CheckBox_01(CheckBox):
    def __init__(self, *args, **kwargs):
        CheckBox.__init__(self, *args, **kwargs)
        self.SetDataLink('', {True: 1, False: 0})

class PdcRow1LinkTable(LinkTable):
    def __init__(self, parent, id):
        LinkTable.__init__(self, parent, id)
        from anag.pdc import PdcDialog
        self.SetDataLink(bt.TABNAME_PDC, "id_pdcrow1", PdcDialog)

class UnoZeroCheckBox(CheckBox):
    def __init__(self, *args, **kwargs):
        CheckBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=(1,0))




# Window functions

ID_ANAGMAIN = 16000
ID_NOTEBOOK = 16001

def CauContabCardFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = AnagCardPanel(parent, -1)
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = WorkZoneNotebook( parent, ID_NOTEBOOK, wx.DefaultPosition, [200,160], 0 )
    item2 = item3
    
    item4 = wx.Panel( item3, -1 )
    Setup1Func(item4, False)
    item3.AddPage( item4, "Setup causale" )

    item5 = wx.Panel( item3, -1 )
    Setup2Func(item5, False)
    item3.AddPage( item5, "Scadenzario e Sottoconti preferiti" )

    item6 = wx.Panel( item3, -1 )
    Setup3Func(item6, False)
    item3.AddPage( item6, "Eventi" )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_TIPREG = 16002
ID_NUMDOC = 16003
ID_NUMIVA = 16004
ID_ESERC = 16005
ID_DATDOC = 16006
ID_PRALCF = 16007
ID_RADIOBOX = 16008
ID_TEXT = 16009
ID_FOREIGN = 16010
ID_BTNMAGREG = 16011
ID_PDCROW1 = 16012
ID_QUAIVANOB = 16013
ID_DAVSCORP = 16014
ID_TEXTCTRL = 16015
ID_CAMSEGR1 = 16016

def Setup1Func( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item2 = RadioBox( parent, ID_TIPREG, "Tipo registrazione", wx.DefaultPosition, wx.DefaultSize, 
        ["Semplice","Composta","Composta con IVA","Gestione solo IVA"] , 1, wx.RA_SPECIFY_COLS )
    item2.SetName( "tipo" )
    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item3 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item4 = RadioBox( parent, ID_NUMDOC, "Numero documento", wx.DefaultPosition, wx.DefaultSize, 
        ["Non gestito","Gestito, non proposto","Gestito, proposto num.protocollo"] , 1, wx.RA_SPECIFY_COLS )
    item4.SetName( "numdoc" )
    item3.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item5 = RadioBox( parent, ID_NUMIVA, "Protocollo IVA", wx.DefaultPosition, wx.DefaultSize, 
        ["Non gestito","Gestito, non proposto","Gestito, proposto num.protocollo"] , 1, wx.RA_SPECIFY_COLS )
    item5.SetName( "numiva" )
    item3.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item3.AddGrowableCol( 0 )

    item3.AddGrowableCol( 1 )

    item3.AddGrowableRow( 0 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item6 = RadioBox( parent, ID_ESERC, "Esercizio", wx.DefaultPosition, wx.DefaultSize, 
        ["In corso","Precedente"] , 1, wx.RA_SPECIFY_COLS )
    item6.SetName( "esercizio" )
    item1.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item7 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item8 = RadioBox( parent, ID_DATDOC, "Data documento", wx.DefaultPosition, wx.DefaultSize, 
        ["Non gestita","Gestita, non proposta","Gestita, proposta data registrazione"] , 1, wx.RA_SPECIFY_COLS )
    item8.SetName( "datdoc" )
    item7.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item9 = RadioBox( parent, ID_PRALCF, "Allegati Clienti/Fornitori", wx.DefaultPosition, wx.DefaultSize, 
        ["Non considera","Incrementa","Diminuisce"] , 1, wx.RA_SPECIFY_COLS )
    item9.SetName( "pralcf" )
    item7.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item7.AddGrowableCol( 1 )

    item1.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.AddGrowableCol( 0 )

    item1.AddGrowableCol( 1 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item10 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item11 = RadioBox( parent, ID_RADIOBOX, "Registro IVA", wx.DefaultPosition, wx.DefaultSize, 
        ["Fisso da causale","Variabile da magazzino"] , 1, wx.RA_SPECIFY_COLS )
    item11.SetName( "regivadyn" )
    item10.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item13 = wx.StaticBox( parent, -1, "" )
    item12 = wx.StaticBoxSizer( item13, wx.VERTICAL )
    
    item14 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item15 = wx.StaticText( parent, ID_TEXT, "Registro IVA fisso:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.SetName( "id_regiva_label" )
    item14.Add( item15, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item16 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item17 = LinkTable(parent, ID_FOREIGN ); item17.SetDataLink( bt.TABNAME_REGIVA, "id_regiva", RegIvaDialog )
    item16.Add( item17, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item18 = wx.Button( parent, ID_BTNMAGREG, "Registri per magazzino", wx.DefaultPosition, wx.DefaultSize, 0 )
    item18.SetName( "_regiva_detmag" )
    item16.Add( item18, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item16.AddGrowableCol( 0 )

    item14.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item19 = wx.StaticText( parent, ID_TEXT, "Sottoconto Partita fisso:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.SetName( "id_regiva_label" )
    item14.Add( item19, 0, wx.ALIGN_CENTER|wx.LEFT, 5 )

    item20 = PdcRow1LinkTable(parent, ID_PDCROW1)
    item14.Add( item20, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item14.AddGrowableCol( 1 )

    item12.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item10.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item10.AddGrowableCol( 1 )

    item0.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item21 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item22 = CheckBox( parent, ID_QUAIVANOB, "Permetti squadratura tra totale sezione IVA e Dare/Avere", wx.DefaultPosition, wx.DefaultSize, 0 )
    item22.SetName( "quaivanob" )
    item21.Add( item22, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item23 = UnoZeroCheckBox( parent, ID_DAVSCORP, "Attiva colonna scorporo su griglia Dare/Avere", wx.DefaultPosition, wx.DefaultSize, 0 )
    item23.SetName( "davscorp" )
    item21.Add( item23, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item24 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item26 = wx.StaticBox( parent, -1, "Partita" )
    item25 = wx.StaticBoxSizer( item26, wx.VERTICAL )
    
    item27 = wx.StaticText( parent, ID_TEXT, "Descrizione:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.Add( item27, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item28 = wx.TextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [200,-1], 0 )
    item28.SetName( "pades" )
    item25.Add( item28, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item29 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item30 = wx.StaticText( parent, ID_TEXT, "Tipo sottoconto:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item29.Add( item30, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item31 = wx.StaticText( parent, ID_TEXT, "Segno:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item29.Add( item31, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item32 = LinkTable(parent, ID_FOREIGN); item32.SetDataLink(bt.TABNAME_PDCTIP, "id_pdctippa", PdcTipDialog )
    item29.Add( item32, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item33 = TextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [24,-1], 0 )
    item33.SetName( "pasegno" )
    item29.Add( item33, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item29.AddGrowableCol( 0 )

    item25.Add( item29, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item34 = CheckBox( parent, ID_CAMSEGR1, "Permetti cambio segno su riga partita", wx.DefaultPosition, wx.DefaultSize, 0 )
    item34.SetName( "camsegr1" )
    item25.Add( item34, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item24.Add( item25, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item36 = wx.StaticBox( parent, -1, "Contropartita" )
    item35 = wx.StaticBoxSizer( item36, wx.VERTICAL )
    
    item37 = wx.StaticText( parent, ID_TEXT, "Descrizione:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item35.Add( item37, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item38 = wx.TextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [200,-1], 0 )
    item38.SetName( "cpdes" )
    item35.Add( item38, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item39 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item40 = wx.StaticText( parent, ID_TEXT, "Tipo sottoconto:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item39.Add( item40, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item41 = LinkTable(parent, ID_FOREIGN); item41.SetDataLink(bt.TABNAME_PDCTIP, "id_pdctipcp", PdcTipDialog)
    item39.Add( item41, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item39.AddGrowableCol( 0 )

    item35.Add( item39, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item24.Add( item35, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item24.AddGrowableCol( 0 )

    item24.AddGrowableCol( 1 )

    item0.Add( item24, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_ATTSCAD = 16017
ID_ATTSC = 16018
ID_SPE = 16019
ID_INS = 16020
ID_PCFSEGNO = 16021
ID_PCFCOL = 16022
ID_PCFABB = 16023
ID_PDCPREF = 16024

def Setup2Func( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.StaticBox( parent, -1, "Scadenzario Clienti/Fornitori" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.FlexGridSizer( 0, 5, 0, 0 )
    
    item5 = wx.StaticBox( parent, -1, "" )
    item4 = wx.StaticBoxSizer( item5, wx.VERTICAL )
    
    item6 = CheckBox( parent, ID_ATTSCAD, "Attiva scadenzario", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.SetName( "pcf" )
    item4.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item7 = CheckBox( parent, ID_ATTSC, "Gestione saldaconto", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.SetName( "pcfscon" )
    item4.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item8 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item9 = CheckBox( parent, ID_SPE, "Spese", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.SetName( "pcfspe" )
    item8.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item10 = CheckBox( parent, ID_INS, "Insoluto", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.SetName( "pcfins" )
    item8.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item4.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item3.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item11 = RadioBox( parent, ID_PCFSEGNO, "", wx.DefaultPosition, wx.DefaultSize, 
        ["Aumenta","Diminuisci"] , 1, wx.RA_SPECIFY_COLS )
    item11.SetName( "pcfsgn" )
    item3.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item12 = RadioBox( parent, ID_PCFCOL, "", wx.DefaultPosition, wx.DefaultSize, 
        ["Nulla","Importo","Pareggiamento"] , 1, wx.RA_SPECIFY_COLS )
    item12.SetName( "pcfimp" )
    item3.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item13 = RadioBox( parent, ID_PCFABB, "", wx.DefaultPosition, wx.DefaultSize, 
        ["Nessun abbuono","Abbuoni attivi","Abbuoni passivi"] , 1, wx.RA_SPECIFY_COLS )
    item13.SetName( "pcfabb" )
    item3.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item3.AddGrowableCol( 0 )

    item3.AddGrowableCol( 1 )

    item3.AddGrowableCol( 2 )

    item3.AddGrowableCol( 3 )

    item3.AddGrowableCol( 4 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item14 = wx.StaticText( parent, ID_TEXT, "Inserire qui i sottoconti più frequentemente utilizzati.", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item15 = wx.StaticText( parent, ID_TEXT, "Saranno proposti automaticamente durante l'iserimento di registrazioni con questa causale.", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item15, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item16 = PdcPrefCauPanel( parent, ID_PDCPREF, wx.DefaultPosition, [200,160], 0 )
    item16.SetName( "panpref" )
    item0.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 3 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_PANGRIDMAG = 16025
ID_BTN_MAGRIV_OK = 16026

def MagRegIvaFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item2 = wx.Panel( parent, ID_PANGRIDMAG, wx.DefaultPosition, [500,160], wx.SUNKEN_BORDER )
    item2.SetName( "pangridpref" )
    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1.AddGrowableCol( 0 )

    item1.AddGrowableRow( 0 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item3 = wx.BoxSizer( wx.HORIZONTAL )
    
    item4 = wx.Button( parent, ID_BTN_MAGRIV_OK, "Conferma", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.GROW|wx.LEFT|wx.RIGHT, 5 )

    item0.Add( item3, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_CURRESERC = 16027
ID_SOVRAPP = 16028
ID_GIOBOLINT = 16029
ID_GIOBOLANN = 16030
ID_GIOBOLPAG = 16031
ID_GIOBOLDAT = 16032
ID_GIOBOLRIG = 16033
ID_LINE = 16034
ID_GIOBOLECD = 16035
ID_GIOBOLECA = 16036
ID_GIOBOLEPD = 16037
ID_GIOBOLEPA = 16038
ID_PANGRIDSTM = 16039
ID_CHIUSURA = 16040
ID_APERTURA = 16041
ID_APECHI_FLAG = 16042
ID_AGGCON = 16043
ID_SAVE = 16044

def ProgressiviFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.StaticBox( parent, -1, "Esercizio" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item4 = wx.StaticText( parent, ID_TEXT, "Esercizio in corso:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item5 = NumCtrl(parent, ID_CURRESERC, integerWidth=4, allowNegative=False, groupDigits=False); item5.SetName("curreserc")
    item3.Add( item5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item6 = CheckBox_01( parent, ID_SOVRAPP, "Sovrapposizione di esercizio attivata", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.SetName( "sovrapp" )
    item3.Add( item6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item8 = wx.StaticBox( parent, -1, "Intestazione giornale" )
    item7 = wx.StaticBoxSizer( item8, wx.VERTICAL )
    
    item9 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item10 = wx.StaticText( parent, ID_TEXT, "Intestazione:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item11 = wx.StaticText( parent, ID_TEXT, "Anno:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.Add( item11, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item12 = wx.StaticText( parent, ID_TEXT, "Pag.:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.Add( item12, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item13 = TextCtrl( parent, ID_GIOBOLINT, "", wx.DefaultPosition, [400,-1], 0 )
    item13.SetName( "giobolint" )
    item9.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item14 = NumCtrl(parent, ID_GIOBOLANN, integerWidth=4, allowNegative=False, groupDigits=False); item14.SetName("giobolann")
    item9.Add( item14, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item15 = NumCtrl(parent, ID_GIOBOLPAG, integerWidth=4, allowNegative=False, groupDigits=False); item15.SetName("giobolpag")
    item9.Add( item15, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item9.AddGrowableCol( 0 )

    item7.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item16 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item18 = wx.StaticBox( parent, -1, "Giornale mastro" )
    item17 = wx.StaticBoxSizer( item18, wx.VERTICAL )
    
    item19 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item20 = wx.StaticText( parent, ID_TEXT, "Data ultima registrazione stampata:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.Add( item20, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item21 = DateCtrl( parent, ID_GIOBOLDAT, "", wx.DefaultPosition, [80,-1], 0 )
    item21.SetName( "gioboldat" )
    item19.Add( item21, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item22 = wx.StaticText( parent, ID_TEXT, "Riga:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.Add( item22, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item23 = NumCtrl(parent, ID_GIOBOLRIG, integerWidth=6, allowNegative=False, groupDigits=False); item23.SetName("giobolrig")
    item19.Add( item23, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item17.Add( item19, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item24 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item17.Add( item24, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item25 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item26 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.Add( item26, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP, 5 )

    item27 = wx.StaticText( parent, ID_TEXT, "DARE", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.Add( item27, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item28 = wx.StaticText( parent, ID_TEXT, "AVERE", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.Add( item28, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item29 = wx.StaticText( parent, ID_TEXT, "Esercizio in corso:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.Add( item29, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item30 = NumCtrl(parent, ID_GIOBOLECD, integerWidth=12, fractionWidth=bt.VALINT_DECIMALS, allowNegative=False, groupDigits=True); item30.SetName("giobolecd")
    item25.Add( item30, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item31 = NumCtrl(parent, ID_GIOBOLECA, integerWidth=12, fractionWidth=bt.VALINT_DECIMALS, allowNegative=False, groupDigits=True); item31.SetName("gioboleca")
    item25.Add( item31, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item32 = wx.StaticText( parent, ID_TEXT, "Precedente:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.Add( item32, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item33 = NumCtrl(parent, ID_GIOBOLEPD, integerWidth=12, fractionWidth=bt.VALINT_DECIMALS, allowNegative=False, groupDigits=True); item33.SetName("giobolepd")
    item25.Add( item33, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item34 = NumCtrl(parent, ID_GIOBOLEPA, integerWidth=12, fractionWidth=bt.VALINT_DECIMALS, allowNegative=False, groupDigits=True); item34.SetName("giobolepa")
    item25.Add( item34, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item17.Add( item25, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item16.Add( item17, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item36 = wx.StaticBox( parent, -1, "Stampa mastri" )
    item35 = wx.StaticBoxSizer( item36, wx.VERTICAL )
    
    item37 = wx.Panel( parent, ID_PANGRIDSTM, wx.DefaultPosition, [160,100], wx.SUNKEN_BORDER )
    item37.SetName( "pangridstm" )
    item35.Add( item37, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item16.Add( item35, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item16.AddGrowableCol( 0 )

    item0.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item39 = wx.StaticBox( parent, -1, "Chiusure" )
    item38 = wx.StaticBoxSizer( item39, wx.VERTICAL )
    
    item40 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item41 = wx.BoxSizer( wx.VERTICAL )
    
    item42 = wx.StaticText( parent, ID_TEXT, "Ultima generazione chiusure:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item41.Add( item42, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item43 = wx.StaticText( parent, ID_TEXT, "Ultima generazione aperture:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item41.Add( item43, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP, 5 )

    item40.Add( item41, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item44 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item45 = wx.BoxSizer( wx.VERTICAL )
    
    item46 = DateCtrl( parent, ID_CHIUSURA, "", wx.DefaultPosition, [80,-1], 0 )
    item46.SetName( "chiusura" )
    item45.Add( item46, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item47 = DateCtrl( parent, ID_APERTURA, "", wx.DefaultPosition, [80,-1], 0 )
    item47.SetName( "apertura" )
    item45.Add( item47, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item44.Add( item45, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item48 = CheckBox_01( parent, ID_APECHI_FLAG, "Movimenti generati per l'esercizio in corso", wx.DefaultPosition, wx.DefaultSize, 0 )
    item48.SetName( "apechi_flag" )
    item44.Add( item48, 0, wx.ALIGN_CENTER|wx.RIGHT|wx.BOTTOM, 5 )

    item40.Add( item44, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item49 = wx.StaticText( parent, ID_TEXT, "Aggiornamento contabile:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item40.Add( item49, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item50 = DateCtrl( parent, ID_AGGCON, "", wx.DefaultPosition, [80,-1], 0 )
    item50.SetName( "aggcon" )
    item40.Add( item50, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item38.Add( item40, 0, wx.ALIGN_CENTER, 5 )

    item0.Add( item38, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item51 = wx.BoxSizer( wx.HORIZONTAL )
    
    item52 = wx.Button( parent, ID_SAVE, "Salva", wx.DefaultPosition, wx.DefaultSize, 0 )
    item51.Add( item52, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item51, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_TIPEVENT = 16045

def Setup3Func( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.StaticBox( parent, -1, "A chiusura registrazione, registra evento" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item4 = wx.StaticText( parent, ID_TEXT, "Tip evento:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item5 = LinkTable(parent, ID_TIPEVENT); item5.SetDataLink(bt.TABNAME_TIPEVENT, "id_tipevent", TipiEventoDialog)
    item3.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3.AddGrowableCol( 1 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "Messaggio da allegare:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item7 = wx.TextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,200], wx.TE_MULTILINE )
    item7.SetFont( wx.Font( 10, wx.MODERN, wx.NORMAL, wx.NORMAL ) )
    item7.SetName( "event_msg" )
    item0.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 2 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
