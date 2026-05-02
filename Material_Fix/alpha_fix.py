import bpy

class MMDMIG_OT_alpha_fix(bpy.types.Operator):
    bl_idname = "mmdmig.alpha_fix"
    bl_label = "Fix Alpha Materials"

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                for mat in obj.data.materials:
                    if mat and mat.use_nodes:
                        mat.blend_method = 'BLEND'
                        mat.shadow_method = 'HASHED'
                        nodes = mat.node_tree.nodes
                        for n in nodes:
                            if n.type == 'BSDF_PRINCIPLED':
                                n.inputs["Alpha"].default_value = 1.0
        return {'FINISHED'}
