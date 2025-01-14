from . import nc
from . import iso_modal
import math
import datetime
import time

now = datetime.datetime.now()

class Creator(iso_modal.Creator):
    def __init__(self):
        iso_modal.Creator.__init__(self)
        self.output_block_numbers = False
        self.output_tool_definitions = False
        self.output_g43_on_tool_change_line = True

    def SPACE(self):
        if self.start_of_line == True:
            self.start_of_line = False
            return ''
        else:
            return ' '

    def PROGRAM(self): return None
    def PROGRAM_END(self):
        if self.output_tool_change:
            # return( 'T0' + self.SPACE() + 'M06' + self.SPACE() + 'M02')
            # WIP modifications for Raptor
            return( 'T0' + self.SPACE() + 'M06' + '\n' + 'M02')
        else:
            return('M02')

    def dwell(self, t):
    	self.write('\n')
    	iso_modal.Creator.dwell(self, t)
############################################################################
## Begin Program


    def program_begin(self, id, comment):
        if (self.useCrc == False):
            self.write( ('(Created with emc2b post processor ' + str(now.strftime("%Y/%m/%d %H:%M")) + ')' + '\n') )
        else:
            self.write( ('(Created with emc2b Cutter Radius Compensation post processor ' + str(now.strftime("%Y/%m/%d %H:%M")) + ')' + '\n') )

        # WIP modifications for Raptor
        self.write( ('%' + '\n') )

        iso_modal.Creator.program_begin(self, id, comment)


nc.creator = Creator()
