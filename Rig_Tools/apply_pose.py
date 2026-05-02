import bpy

class MMDMIG_OT_apply_pose(bpy.types.Operator):
    bl_idname = "mmdmig.apply_pose"
    bl_label = "Apply Pose as Rest"

    def execute(self, context):
        obj = context.object
        if obj and obj.type == 'ARMATURE':
            bpy.ops.object.mode_set(mode='POSE')
            bpy.ops.pose.armature_apply()
            bpy.ops.object.mode_set(mode='OBJECT')
        return {'FINISHED'}
