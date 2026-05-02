import bpy
import random

class MMDMIG_OT_matcap(bpy.types.Operator):
    bl_idname = "mmdmig.create_matcap"
    bl_label = "Create HDR + Matcap"

    def execute(self, context):

        world = bpy.data.worlds.get("MMDMig_HDR")
        if not world:
            world = bpy.data.worlds.new("MMDMig_HDR")

        world.use_nodes = True
        nodes = world.node_tree.nodes
        links = world.node_tree.links

        nodes.clear()

        output = nodes.new(type='ShaderNodeOutputWorld')
        bg = nodes.new(type='ShaderNodeBackground')
        tex = nodes.new(type='ShaderNodeTexEnvironment')
        mapping = nodes.new(type='ShaderNodeMapping')
        coord = nodes.new(type='ShaderNodeTexCoord')

        mapping.inputs[2].default_value[2] = random.uniform(0, 6.28)

        links.new(coord.outputs['Generated'], mapping.inputs['Vector'])
        links.new(mapping.outputs['Vector'], tex.inputs['Vector'])
        links.new(tex.outputs['Color'], bg.inputs['Color'])
        links.new(bg.outputs['Background'], output.inputs['Surface'])

        context.scene.world = world

        mat = bpy.data.materials.new(name="MMDMig_Matcap")
        mat.use_nodes = True

        nodes = mat.node_tree.nodes
        links = mat.node_tree.links

        nodes.clear()

        output = nodes.new(type='ShaderNodeOutputMaterial')
        emission = nodes.new(type='ShaderNodeEmission')
        layer_weight = nodes.new(type='ShaderNodeLayerWeight')
        mix = nodes.new(type='ShaderNodeMixRGB')

        mix.blend_type = 'ADD'

        links.new(layer_weight.outputs['Facing'], mix.inputs['Fac'])
        links.new(layer_weight.outputs['Facing'], emission.inputs['Strength'])
        links.new(emission.outputs['Emission'], output.inputs['Surface'])

        obj = context.object
        if obj and obj.type == 'MESH':
            obj.data.materials.append(mat)

        return {'FINISHED'}