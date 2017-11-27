#python
import lx
import lxu.command

class CMD_toggle(lxu.command.BasicCommand):
    
    _var = False
    
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        
        self.dyna_Add('state', lx.symbol.sTYPE_BOOLEAN)
        self.basic_SetFlags(0, lx.symbol.fCMDARG_OPTIONAL | lx.symbol.fCMDARG_QUERY)
    
    def cmd_Flags(self):
        return lx.symbol.fCMD_UI

    def basic_Execute(self, msg, flags):
        CMD_toggle._var = not self._var

    def basic_Enable(self, msg):
        return True

    def cmd_Query(self, index, vaQuery):
        if index == 0:
            va = lx.object.ValueArray (vaQuery)
            va.AddInt (self._var)

lx.bless(CMD_toggle, "cmd.toggle")