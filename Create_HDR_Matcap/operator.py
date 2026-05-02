import bpy

class MMDMIG_OT_matcap(bpy.types.Operator):
    bl_idname = "mmdmig.create_matcap"
    bl_label = "Create HDR Matcap"

    def execute(self, context):
        mat = bpy.data.materials.new(name="MMDMig_Matcap")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links

        nodes.clear()

        output = nodes.new(type='ShaderNodeOutputMaterial')
        emission = nodes.new(type='ShaderNodeEmission')
        tex = nodes.new(type='ShaderNodeTexEnvironment')

        links.new(tex.outputs[0], emission.inputs[0])
        links.new(emission.outputs[0], output.inputs[0])

        if context.object:
            if context.object.data.materials:
                context.object.data.materials[0] = mat
            else:
                context.object.data.materials.append(mat)

        return {'FINISHED'}
