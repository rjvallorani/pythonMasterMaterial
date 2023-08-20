import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

masterMaterialStacked = AssetTools.create_asset("M_Master_Stacked", "/Game/MasterMaterials", unreal.Material, unreal.MaterialFactoryNew())

#Create 2D Texture Param and Connect to Base Color
baseColorTextureParam = MaterialEditLibrary.create_material_expression(masterMaterialStacked, unreal.MaterialExpressionTextureSampleParameter, -384, -200)
MaterialEditLibrary.connect_material_property(baseColorTextureParam, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)

#Create Constant and Connect to Specular
specParam = MaterialEditLibrary.create_material_expression(masterMaterialStacked, unreal.MaterialExpressionConstant, -384, 200)
specParam.set_editor_property("R", 0.3)
MaterialEditLibrary.connect_material_property(specParam, "", unreal.MaterialProperty.MP_SPECULAR)

#Create 2D Texture Param and Connect to Normal
normalTextureParam = MaterialEditLibrary.create_material_expression(masterMaterialStacked, unreal.MaterialExpressionTextureSampleParameter, -384, 300)
MaterialEditLibrary.connect_material_property(normalTextureParam, "RGB", unreal.MaterialProperty.MP_NORMAL)

#Create 2D Texture Param and Connect to Ambient Occlusion, Roughness, and Metallic
ormTextureParam = MaterialEditLibrary.create_material_expression(masterMaterialStacked, unreal.MaterialExpressionTextureSampleParameter, -384, 500)
MaterialEditLibrary.connect_material_property(ormTextureParam, "R", unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)
MaterialEditLibrary.connect_material_property(ormTextureParam, "G", unreal.MaterialProperty.MP_ROUGHNESS)
MaterialEditLibrary.connect_material_property(ormTextureParam, "B", unreal.MaterialProperty.MP_METALLIC)

#Create Material Instance
stackedMatInstance = AssetTools.create_asset("masterMatStacked_ORM_Inst", "/Game/MasterMaterials", unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())
#stackedMatInstance.set_editor_property(unreal.MaterialInstanceConstant)

EditorAssetLibrary.save_asset("/Game/MasterMaterials/M_Master_Stacked", True)
EditorAssetLibrary.save_asset("/Game/MasterMaterials/masterMatStacked_ORM_Inst", True)