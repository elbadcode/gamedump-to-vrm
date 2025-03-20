from bpy import context
# just run this from text editor after importing a mesh and applying diffuse textures

for mat in bpy.data.materials:
    mat.vrm_addon_extension.mtoon1.enabled = True


for arma in bpy.data.armatures:
    arma.vrm_addon_extension.spec_version = '1.0'



