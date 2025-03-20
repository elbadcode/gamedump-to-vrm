# SPDX-License-Identifier: MIT OR GPL-3.0-or-later
from ..vrm1.human_bone import HumanBoneSpecification, HumanBoneSpecifications

mapping: dict[str, HumanBoneSpecification] = {
"pelvis" : HumanBoneSpecifications.HIPS
"spine_01" : HumanBoneSpecifications.SPINE
"spine_04" : HumanBoneSpecifications.CHEST
"neck_01" : HumanBoneSpecifications.NECK
"head" : HumanBoneSpecifications.HEAD
"facial_Eye01_r" : HumanBoneSpecifications.RIGHT_EYE
"facial_Eye01_l" : HumanBoneSpecifications.LEFT_EYE
"clavicle_r" : HumanBoneSpecifications.RIGHT_SHOULDER
"upperarm_r" : HumanBoneSpecifications.RIGHT_UPPER_ARM
"lowerarm_r" : HumanBoneSpecifications.RIGHT_LOWER_ARM
"hand_r" : HumanBoneSpecifications.RIGHT_HAND
"clavicle_l" : HumanBoneSpecifications.LEFT_SHOULDER
"upperarm_l" : HumanBoneSpecifications.LEFT_UPPER_ARM
"lowerarm_l" : HumanBoneSpecifications.LEFT_LOWER_ARM
"hand_l" : HumanBoneSpecifications.LEFT_HAND
"thigh_r" : HumanBoneSpecifications.RIGHT_UPPER_LEG
"calf_r" : HumanBoneSpecifications.RIGHT_LOWER_LEG
"foot_r" : HumanBoneSpecifications.RIGHT_FOOT
"ball_r" : HumanBoneSpecifications.RIGHT_TOES
"thigh_l" : HumanBoneSpecifications.LEFT_UPPER_LEG
"calf_l" : HumanBoneSpecifications.LEFT_LOWER_LEG
"foot_l" : HumanBoneSpecifications.LEFT_FOOT
"ball_l" : HumanBoneSpecifications.LEFT_TOES
"thumb_01_r" : HumanBoneSpecifications.RIGHT_THUMB_METACARPAL
"thumb_02_r" : HumanBoneSpecifications.RIGHT_THUMB_PROXIMAL
"thumb_03_r" : HumanBoneSpecifications.RIGHT_THUMB_DISTAL
"thumb_01_l" : HumanBoneSpecifications.LEFT_THUMB_METACARPAL
"thumb_02_l" : HumanBoneSpecifications.LEFT_THUMB_PROXIMAL
"thumb_03_l" : HumanBoneSpecifications.LEFT_THUMB_DISTAL
"index_01_r" : HumanBoneSpecifications.RIGHT_INDEX_PROXIMAL
"index_02_r" : HumanBoneSpecifications.RIGHT_INDEX_INTERMEDIATE
"index_03_r" : HumanBoneSpecifications.RIGHT_INDEX_DISTAL
"index_01_l" : HumanBoneSpecifications.LEFT_INDEX_PROXIMAL
"index_02_l" : HumanBoneSpecifications.LEFT_INDEX_INTERMEDIATE
"index_03_l" : HumanBoneSpecifications.LEFT_INDEX_DISTAL
"middle_01_r" : HumanBoneSpecifications.RIGHT_MIDDLE_PROXIMAL
"middle_02_r" : HumanBoneSpecifications.RIGHT_MIDDLE_INTERMEDIATE
"middle_03_r" : HumanBoneSpecifications.RIGHT_MIDDLE_DISTAL
"middle_01_l" : HumanBoneSpecifications.LEFT_MIDDLE_PROXIMAL
"middle_02_l" : HumanBoneSpecifications.LEFT_MIDDLE_INTERMEDIATE
"middle_03_l" : HumanBoneSpecifications.LEFT_MIDDLE_DISTAL
"ring_01_r" : HumanBoneSpecifications.RIGHT_RING_PROXIMAL
"ring_02_r" : HumanBoneSpecifications.RIGHT_RING_INTERMEDIATE
"ring_03_r" : HumanBoneSpecifications.RIGHT_RING_DISTAL
"ring_01_l" : HumanBoneSpecifications.LEFT_RING_PROXIMAL
"ring_02_l" : HumanBoneSpecifications.LEFT_RING_INTERMEDIATE
"ring_03_l" : HumanBoneSpecifications.LEFT_RING_DISTAL
"pinky_01_r" : HumanBoneSpecifications.RIGHT_LITTLE_PROXIMAL
"pinky_02_r" : HumanBoneSpecifications.RIGHT_LITTLE_INTERMEDIATE
"pinky_03_r" : HumanBoneSpecifications.RIGHT_LITTLE_DISTAL
"pinky_01_l" : HumanBoneSpecifications.LEFT_LITTLE_PROXIMAL
"pinky_02_l" : HumanBoneSpecifications.LEFT_LITTLE_INTERMEDIATE
"pinky_03_l" : HumanBoneSpecifications.LEFT_LITTLE_DISTAL
}



config_ue = ("unreal(VRM1)", mapping)
