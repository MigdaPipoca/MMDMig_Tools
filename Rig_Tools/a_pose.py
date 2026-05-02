import bpy
import math

class MMDMIG_OT_a_pose(bpy.types.Operator):
    bl_idname = "mmdmig.a_pose"
    bl_label = "Apply A-Pose"

    def execute(self, context):
        obj = context.object
        if obj and obj.type == 'ARMATURE':
            bpy.ops.object.mode_set(mode='POSE')

            for bone in obj.pose.bones:
                if "arm" in bone.name.lower():
                    bone.rotation_mode = 'XYZ'
                    bone.rotation_euler[2] = math.radians(20)

            bpy.ops.object.mode_set(mode='OBJECT')
        return {'FINISHED'}
