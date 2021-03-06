# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: stati.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
from anag.basetab import AnagCardPanel

from awc.controls.linktable import LinkTable
from awc.controls.radiobox import RadioBox
from awc.controls.checkbox import UnoZeroCheckBox
from awc.controls.textctrl import TextCtrl, TextCtrl_LC

from awc.controls.attachbutton import AttachmentButton

from Env import Azienda
bt = Azienda.BaseTab



# Window functions

ID_ANAGMAIN = 16000
ID_TEXT = 16001
ID_DESCENG = 16002
ID_VATPREFIX = 16003
ID_CODUNICO = 16004
ID_IS_CEE = 16005
ID_IS_BLACKLISTED = 16006

def StatiFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = AnagCardPanel(parent)
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item3 = wx.StaticText( parent, ID_TEXT, "Descrizione inglese:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item3, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item4 = TextCtrl( parent, ID_DESCENG, "", wx.DefaultPosition, [80,-1], 0 )
    item4.SetName( "desceng" )
    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = wx.StaticText( parent, ID_TEXT, "Prefisso VAT Numbers:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item6 = TextCtrl( parent, ID_VATPREFIX, "", wx.DefaultPosition, [40,-1], 0 )
    item6.SetName( "vatprefix" )
    item2.Add( item6, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Cod. Unico:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item8 = TextCtrl( parent, ID_CODUNICO, "", wx.DefaultPosition, [40,-1], 0 )
    item8.SetName( "codunico" )
    item2.Add( item8, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item2.Add( [ 20, 20 ] , 0, wx.ALIGN_CENTER, 5 )

    item9 = UnoZeroCheckBox( parent, ID_IS_CEE, "Stato membro CEE", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.SetName( "is_cee" )
    item2.Add( item9, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item2.Add( [ 20, 20 ] , 0, wx.ALIGN_CENTER, 5 )

    item10 = UnoZeroCheckBox( parent, ID_IS_BLACKLISTED, "Stato presente in blacklist acquisti/vendite", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.SetName( "is_blacklisted" )
    item2.Add( item10, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item2.AddGrowableCol( 1 )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( [ 20, 150 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
