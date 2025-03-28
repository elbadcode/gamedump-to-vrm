from os.path import join, isdir, isfile
import json
from os import scandir, environ, makedirs,rename,chdir
from os.path import join, isdir, isfile, dirname, basename, abspath
from shutil import copyfile

import bpy
import math
import itertools
from enum import Enum
from bpy.types import Armature, Object
from bpy import context






def ascii_letters(string):
    # these numbers simply correspond to lowercase a-z and thus we have an easy oneliner to get only letters
    return ''.join(x for x in string if (97 <= ord(x) <= 122))

def apply_texture(obj, texture_path, mats):
# Create a new material if the object doesn't have one
    for mat in mats:
        if ascii_letters(mat) in ascii_letters(texture_path) and ascii_letters(texture_path).endswith("Dpng"):
            material = bpy.data.materials.new(name="Material")
            obj.data.materials.append(material)
            # Enable 'Use Nodes'
            material.use_nodes = True
            nodes = material.node_tree.nodes
            material.name = "MI_"+ascii_letters(texture_path).split('T')[1].split('D')[0]
            # Clear default nodes
            for node in nodes:
                nodes.remove(node)

            # Create nodes
            bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
            texture = nodes.new(type='ShaderNodeTexImage')

            texture.image = bpy.data.images.load(texture_path)
            texture.image.alpha_mode ='PREMUL'
            output = nodes.new(type='ShaderNodeOutputMaterial')
            # Position nodes
            texture.location = (-300, 0)
            bsdf.location = (0, 0)
            output.location = (300, 0)

            # Link nodes
            links = material.node_tree.links
            links.new(texture.outputs['Color'], bsdf.inputs['Base Color'])
            links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])


def apply_texture2(obj, texture_path):
    # Create a new material if the object doesn't have one
    for material in obj.data.materials:
        if material.name == "MI_"+basename(texture_path).replace("_D","").replace("T_","").rsplit(".")[0]:

            
            # Enable 'Use Nodes'
            material.use_nodes = True
            nodes = material.node_tree.nodes
            
            # Clear default nodes
            for node in nodes:
                nodes.remove(node)

            # Create nodes
            bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
            texture = nodes.new(type='ShaderNodeTexImage')
            try:
                normtexture = nodes.new(type='ShaderNodeTexImage')
                normtexture.image = bpy.data.images.load(str(texture_path).replace("_D","_N"))
                normtexture.image.colorspace_settings.name = 'Non-Color'
            except Exception as e:
                pass
            texture.image = bpy.data.images.load(texture_path)
            texture.image.alpha_mode ='PREMUL'
            output = nodes.new(type='ShaderNodeOutputMaterial')
            # Position nodes
            texture.location = (-300, 0)
            bsdf.location = (0, 0)
            output.location = (300, 0)

            # Link nodes
            links = material.node_tree.links
            links.new(texture.outputs['Color'], bsdf.inputs['Base Color'])
            links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])



def get_tex(spath):
    try:
        textures = ([f.path for f in scandir(spath) if f.name.endswith(".png")])
        for _dir in scandir(spath):
            if isdir(_dir):
                textures.extend(get_tex(_dir.path))
    except Exception as e:
        pass
    return textures
#textures = get_tex("H:\\dump\\Exports\\Marvel\\Content\\Marvel\\Characters\\1031\\1031001\\texture")

#mats = [f.name for f in scandir("H:\\dump\\Exports\\Marvel\\Content\\Marvel\\Characters\\1031\\1031001\\materials") if isfile(f.path)]
#for m in mats:print(m)


def imports():
    base = "H:\\dump\\Exports\\ProjectT\\Content\\Mesh\\NPC\\SKM\\Talent"
    #char = str(nn).rsplit("\\")[-2]
    #print(char)
    obj1 = bpy.context.object
    collection = obj1.users_collection[0]

    for obj in bpy.context.editable_objects:
        try:
            name = str(obj.name).rsplit('_')[-2]
            texpath = join(base, name, "Texture")
            
            textures = [f.path for f in scandir(texpath) if f.name.endswith("D.png")]
            for t in textures:
                apply_texture2(obj, t)
        except Exception as e:
            pass


def make_vrm():
    
    try:
        for mat in bpy.data.materials:
            mat.vrm_addon_extension.mtoon1.enabled = True
            im = mat.vrm_addon_extension.mtoon1.pbr_metallic_roughness.base_color_texture.index.source
            mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.shade_multiply_texture.index.source = bpy.data.images[im.name]
            mat.vrm_addon_extension.mtoon1.alpha_mode = 'MASK'
            mat.vrm_addon_extension.mtoon1.normal_texture.index.source = bpy.data.images[str(im.name).replace("_D","_N")]
            mat.vrm_addon_extension.mtoon1.alpha_cutoff = 0.1
        for arma in bpy.data.armatures:
            arma.vrm_addon_extension.spec_version = '1.0'
    except Exception as e:
        pass
    
obj1 = bpy.context.object
collection = obj1.users_collection[0]
objects = collection.all_objects
imports()
for mat in bpy.data.materials:
    mat.vrm_addon_extension.mtoon1.enabled = True
    try:
        im = mat.vrm_addon_extension.mtoon1.pbr_metallic_roughness.base_color_texture.index.source
        mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.shade_multiply_texture.index.source = bpy.data.images[im.name]
        mat.vrm_addon_extension.mtoon1.alpha_mode = 'MASK'
        
        mat.vrm_addon_extension.mtoon1.normal_texture.index.source = bpy.data.images[str(im.name).replace("_D","_N")]
    except Exception as e:
        pass
    mat.vrm_addon_extension.mtoon1.alpha_cutoff = 0.1

for arma in bpy.data.armatures:
    arma.vrm_addon_extension.spec_version = '1.0'



