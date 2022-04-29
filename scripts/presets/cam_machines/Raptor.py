import bpy
d = bpy.context.scene.cam_machine
s = bpy.context.scene.unit_settings

d.post_processor = 'RAPTOR'
s.system = 'METRIC'
d.use_position_definitions = False
d.starting_position = (0.0, 0.0, 0.0)
d.mtc_position = (0.0, 0.0, 0.0)
d.ending_position = (0.0, 0.0, 0.0)
d.working_area = (3.25, 2.5, 0.20000000298023224)
d.feedrate_min = 1.0
d.feedrate_max = 5.0
d.feedrate_default = 3.000000238418579
d.spindle_min = 5000.0
d.spindle_max = 30000.0
d.spindle_default = 18000.0
d.axis4 = False
d.axis5 = False
d.collet_size = 0.032999999821186066
d.output_tool_change = False
d.output_block_numbers = False
d.output_tool_definitions = True
d.output_g43_on_tool_change = False
