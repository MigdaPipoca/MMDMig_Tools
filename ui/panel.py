import bpy

class MMDMIG_PT_panel(bpy.types.Panel):
    bl_label = "MMDMig Tools"
    bl_idname = "MMDMIG_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MMDMig Tools"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "mmdmig_category", expand=True)

        if scene.mmdmig_category == 'GENERAL':
            box = layout.box()
            box.operator("mmdmig.plain_axes")
            box.operator("mmdmig.smooth_normals")

        elif scene.mmdmig_category == 'MATERIAL':
            box = layout.box()
            box.operator("mmdmig.create_matcap")
            box.operator("mmdmig.alpha_fix")

        elif scene.mmdmig_category == 'RIG':
            box = layout.box()
            box.operator("mmdmig.apply_pose")
            box.operator("mmdmig.a_pose")

        elif scene.mmdmig_category == 'EXTRA':
            box = layout.box()
            box.label(text="More tools soon")
