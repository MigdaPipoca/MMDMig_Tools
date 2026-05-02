import bpy

class MMDMIG_OT_plain_axes(bpy.types.Operator):
    bl_idname = "mmdmig.plain_axes"
    bl_label = "Convert to Plain Axes"

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type == 'EMPTY':
                obj.empty_display_type = 'PLAIN_AXES'
        return {'FINISHED'}
