import bpy

# Initialize variables
arma = None

# Get the active object
obj = bpy.context.object

# Ensure the object is a mesh
if obj.type == 'MESH':
    for modifier in obj.modifiers:
        if modifier.type == 'ARMATURE':  # Check if the modifier is an armature
            armature_modifier = modifier
            arma = armature_modifier.object
            break

# Ensure an armature was found
if not arma:
    raise Exception("No armature modifier found on the mesh object.")

# Get the armature data
arma_data = arma.data

# Deselect all objects
bpy.ops.object.select_all(action='DESELECT')

# Select the armature and set it as the active object
arma.select_set(True)
bpy.context.view_layer.objects.active = arma

# Switch to Pose Mode
bpy.ops.object.mode_set(mode='POSE')

# Select all bones in Pose Mode
bpy.ops.pose.select_all(action='SELECT')

# Collect IK target bone names
ik_bone_names = []
for pose_bone in bpy.context.object.pose.bones:
    try:
        for constraint in pose_bone.constraints:
            if constraint.type == "IK" and constraint.subtarget in pose_bone.id_data.pose.bones:
                ik_bone_names.append(constraint.subtarget)
        if 'IK' in pose_bone.name:
            ik_bone_names.append(pose_bone) 
    except Exception as e:
        pass
bpy.ops.object.mode_set(mode='EDIT')


for edit_bone in bpy.context.editable_bones:
    if 'IK' in edit_bone.name:
        ik_bone_names.append(pose_bone) 
for ik_bone in ik_bone_names:
    print(ik_bone)
# Switch to Edit Mode

# Filter bones to remove (those in ik_bone_names)
bones_to_remove = [bone for bone in arma_data.edit_bones if bone.name in ik_bone_names]

# Sort bones by hierarchy depth (remove child bones first)
bones_to_remove.sort(key=lambda b: b.parent is not None)

# Remove bones in the sorted order
for bone in bones_to_remove:
    arma_data.edit_bones.remove(bone)

print(f"Removed {len(bones_to_remove)} bones.")
