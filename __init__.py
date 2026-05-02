bl_info = {
    "name": "MMDMig Tools",
    "author": "Miguel",
    "version": (1, 0, 0),
    "blender": (4, 5, 0),
    "category": "Object"
}

import bpy
from .PlainAxes_Conversion.operator import MMDMIG_OT_plain_axes
from .Create_HDR_Matcap.operator import MMDMIG_OT_matcap
from .Material_Fix.alpha_fix import MMDMIG_OT_alpha_fix
from .Rig_Tools.apply_pose import MMDMIG_OT_apply_pose
from .Mesh_Fix.smooth_normals import MMDMIG_OT_smooth_normals
from .Rig_Tools.a_pose import MMDMIG_OT_a_pose
from .ui.panel import MMDMIG_PT_panel
from .core.translation import register_translation, unregister_translation

classes = (
    MMDMIG_OT_plain_axes,
    MMDMIG_OT_matcap,
    MMDMIG_OT_alpha_fix,
    MMDMIG_OT_apply_pose,
    MMDMIG_OT_smooth_normals,
    MMDMIG_OT_a_pose,
    MMDMIG_PT_panel,
)

def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.Scene.mmdmig_category = bpy.props.EnumProperty(
        name="Category",
        items=[
            ('GENERAL', "General", ""),
            ('MATERIAL', "Material", ""),
            ('RIG', "Rig", ""),
            ('EXTRA', "Extra", "")
        ],
        default='GENERAL'
    )

    register_translation()

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

    del bpy.types.Scene.mmdmig_category

    unregister_translation()
