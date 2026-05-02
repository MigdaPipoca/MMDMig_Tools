import bpy

class MMDMIG_OT_smooth_normals(bpy.types.Operator):
    bl_idname = "mmdmig.smooth_normals"
    bl_label = "Fix Normals"

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.shade_smooth()
                obj.data.use_auto_smooth = True
                obj.data.auto_smooth_angle = 3.14159
        return {'FINISHED'}
