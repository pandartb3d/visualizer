bl_info = {
    "name": "visualizer",
    "author": "pandartb3d",
    "version": (1, 1),
    "blender": (2, 82, 0),
    "location": "View3D",
    "description": "Generate",
    "warning": "",
    "wiki_url": "https://github.com/pandartb3d/visualizer",
    "category": "3D View",
}

import bpy
import os
from bpy.props import IntProperty
from bpy.types import Panel

from bpy.props import StringProperty
from bpy.props import *

bpy.types.Scene.MyInt = IntProperty( name="MyInt", 
                                       description="MyInt", 
                                       min=0, max=360, default=0)


class RotHDRI(bpy.types.Operator):
    bl_idname = "scene.rothdri"
    bl_label = "Rot HDRI"
    
    
    def execute(self, context):
        context = bpy.context
        scene = context.scene

        bpy.data.worlds['World'].node_tree.nodes["Mapping"].inputs[2].default_value[2] = scene.MyInt
        
        return {"FINISHED"}
    
    
    
    
    

class ImportObj(bpy.types.Operator):
    bl_idname = "scene.importobj"
    bl_label = "Import .obj"
    
    def execute(self, context):
        context = bpy.context
        scene = context.scene

        bpy.ops.import_scene.obj('INVOKE_DEFAULT')
        return {"FINISHED"}

class SaveFile(bpy.types.Operator):
    bl_idname = "scene.savefile"
    bl_label = "Save File"
    
    def execute(self, context):
        context = bpy.context
        scene = context.scene

        bpy.ops.wm.save_as_mainfile('INVOKE_DEFAULT')

        return {"FINISHED"}

class ResetStartupFile(bpy.types.Operator):
    bl_idname = "scene.resetstartupfile"
    bl_label = "Reset Startup File"
    
    def execute(self, context):
        context = bpy.context
        scene = context.scene

        addon_path = bpy.utils.user_resource('SCRIPTS', "addons")
        template_path = "visualizer-master\\template.blend"
        temp_path = "visualizer-master\\temp.blend"

        full_path = os.path.join(addon_path, template_path)
        full_path_temp = os.path.join(addon_path, temp_path)
        

        bpy.ops.wm.open_mainfile(filepath=full_path)


        bpy.ops.wm.save_as_mainfile(filepath=full_path_temp)
        
        return {"FINISHED"}
    
class Resolution(bpy.types.Operator):
    bl_idname = "scene.resolution"
    bl_label = "Resolution"
    
    var1 = IntProperty(default=100)
    
    def execute(self, context):
        context = bpy.context
        scene = context.scene
        bpy.data.scenes["Scene"].render.resolution_percentage = self.var1
        return {"FINISHED"}
    
class Qualitat(bpy.types.Operator):
    bl_idname = "scene.qualitat"
    bl_label = "Qualitat"
    
    var2 = IntProperty(default=100)
    
    def execute(self, context):
        context = bpy.context
        scene = context.scene
        bpy.data.scenes["Scene"].cycles.samples = self.var2
        return {"FINISHED"}
    
class Preview(bpy.types.Operator):
    bl_idname = "scene.preview"
    bl_label = "Preview"
    
    var3 = StringProperty(default="Material Preview")
    
    def execute(self, context):
        context = bpy.context
        scene = context.scene
        bpy.context.space_data.shading.type = self.var3
        return {"FINISHED"}
    
class Smooth(bpy.types.Operator):
    bl_idname = "scene.smooth"
    bl_label = "Smooth Shading"
    
   
    
    def execute(self, context):
        context = bpy.context
        scene = context.scene
        bpy.context.object.data.use_auto_smooth = True
        bpy.ops.object.shade_smooth()

        return {"FINISHED"}
    
class SelectAll(bpy.types.Operator):
    bl_idname = "scene.selectall"
    bl_label = "Select All"
    
   
    
    def execute(self, context):
        context = bpy.context
        scene = context.scene
        bpy.ops.object.select_all(action='SELECT')
        return {"FINISHED"}
    
class Cam(bpy.types.Operator):
    bl_idname = "scene.cam"
    bl_label = "Camera"
    
   
    
    def execute(self, context):
        context = bpy.context
        scene = context.scene
        bpy.ops.view3d.view_camera()
        return {"FINISHED"}
    
    
    

class Instruction(bpy.types.Operator):
    bl_idname = "scene.instruction"
    bl_label = "Instruction"
    
    def execute(self, context):
        context = bpy.context
        scene = context.scene

        addon_path = bpy.utils.user_resource('SCRIPTS', "addons")
        instruction_path = "visualizer-master/instruction.pdf"

        full_path_instruction = os.path.join(addon_path, instruction_path)

        bpy.ops.wm.path_open(filepath=full_path_instruction)
        return {"FINISHED"}

class Materials(bpy.types.Operator):
    bl_idname = "scene.materials"
    bl_label = "Materials"
    
    def execute(self, context):
        context = bpy.context
        scene = context.scene

        addon_path = bpy.utils.user_resource('SCRIPTS', "addons")
        instruction_path = "visualizer-master/materials.jpg"

        full_path_instruction = os.path.join(addon_path, instruction_path)

        bpy.ops.wm.path_open(filepath=full_path_instruction)
        return {"FINISHED"}
    
class Folder(bpy.types.Operator):
    bl_idname = "scene.folder"
    bl_label = "Folder"
    
    def execute(self, context):
        context = bpy.context
        scene = context.scene
        
        filepath = bpy.data.filepath
        relpath = bpy.path.relpath(filepath)
        path = filepath[0: -1 * (relpath.__len__() - 2)]

        bpy.ops.wm.path_open(filepath=path)
        return {"FINISHED"}
    
class ChangeHDRI(bpy.types.Operator):
    bl_idname = "scene.changehdri"
    bl_label = "Change HDRI"
    
    var4 = StringProperty(default="courtyard.exr")
    
    def execute(self, context):
        
        path1 = bpy.utils.system_resource('DATAFILES',"studiolights")
        hdri_folder = 'world/'
        
        
        
        full_path_hdri_folder = os.path.join(path1, hdri_folder)
        
        
        full_path_hdri = os.path.join(full_path_hdri_folder, self.var4)
        
        
        
        test = bpy.data.images.load(full_path_hdri)
        
        bpy.data.worlds['World'].node_tree.nodes['Environment Texture'].image = test
        return {"FINISHED"}

class ReplaceMaterial(bpy.types.Operator):
    bl_idname = "scene.replacematerial"
    bl_label = "Replace Material"
    
    var5 = StringProperty(default="lib_default")
    
    def execute(self, context):
        
        mat = bpy.data.materials.get(self.var5)

        bpy.ops.object.select_linked(type='MATERIAL')

        sel = bpy.context.selected_objects

        for ob in sel:
            if ob.data.materials:
                # assign to 1st material slot
                ob.data.materials[0] = mat
            else:
                # no slots
                ob.data.materials.append(mat)
        bpy.ops.object.select_all(action='DESELECT')



        return {"FINISHED"}
      
    
    
    

class panel(bpy.types.Panel):
    bl_idname = "panel.panel1"
    bl_label = "Visualizer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Visualizer"
 
    def draw(self, context):
        
        layout = self.layout
        obj = context.object
        scn = context.scene
        
        


        
        row = layout.row(align=True)
        row.label(text="visualizer 1.1 - 21.02.2020")
        row = layout.row()
        row.operator("scene.resetstartupfile", text = "Load Template", icon='FILE_REFRESH')
        row = layout.row()
        row.operator("scene.savefile", icon='EXPORT')

        row = layout.row()
        row.operator("scene.importobj", icon='IMPORT')

        
        row = layout.row()
        row = layout.row()
        row = layout.row()

        row.operator("scene.selectall", icon='RESTRICT_SELECT_OFF')
        
        
        row = layout.row()  
        row.label(text="Material Presets:")
        row = layout.row()
        op5 = row.operator("scene.replacematerial",text='lib_default_metal')
        op5.var5 = "lib_default_metal"
        op5 = row.operator("scene.replacematerial",text='lib_copper')
        op5.var5 = "lib_copper"
        op5 = row.operator("scene.replacematerial",text='lib_brass')
        op5.var5 = "lib_brass"
        op5 = row.operator("scene.replacematerial",text='lib_metal_rough')
        op5.var5 = "lib_metal_rough"
        row = layout.row()  
        op5 = row.operator("scene.replacematerial",text='lib_plastic_gloss')
        op5.var5 = "lib_plastic_gloss"
        op5 = row.operator("scene.replacematerial",text='lib_plastic_soft')
        op5.var5 = "lib_plastic_soft"
        op5 = row.operator("scene.replacematerial",text='lib_plastic_rough')
        op5.var5 = "lib_plastic_rough"
        row = layout.row() 
        op5 = row.operator("scene.replacematerial",text='lib_emission')
        op5.var5 = "lib_emission"
        op5 = row.operator("scene.replacematerial",text='lib_glass')
        op5.var5 = "lib_glass"
        
        row = layout.row()  
        row.operator("scene.materials",text='Preview', icon='MATERIAL')
        row = layout.row() 
        row.label(text="Custome Material:")
        row = layout.row()
        row.label(text="")
        row.label(text="go to ------>")
        row.label(icon='MATERIAL')
        row = layout.row()
        row.label(text="Smooth: (select only one object)")
        row = layout.row()
        row.operator("scene.smooth", icon='MOD_SMOOTH')
        row = layout.row()
        row.label(text="Lighting")
        row = layout.row()
        op4 = row.operator("scene.changehdri",text='courtyard')
        op4.var4 = "courtyard.exr"
        op4 = row.operator("scene.changehdri",text='city')
        op4.var4 = "city.exr"
        op4 = row.operator("scene.changehdri",text='forest')
        op4.var4 = "forest.exr"
        op4 = row.operator("scene.changehdri",text='interior')
        op4.var4 = "interior.exr"
        row = layout.row()
        op4 = row.operator("scene.changehdri",text='night')
        op4.var4 = "night.exr"
        op4 = row.operator("scene.changehdri",text='studio')
        op4.var4 = "studio.exr"
        op4 = row.operator("scene.changehdri",text='sunrise')
        op4.var4 = "sunrise.exr"
        op4 = row.operator("scene.changehdri",text='sunset')
        op4.var4 = "sunset.exr"
        row = layout.row()
        row.prop(scn, "MyInt", slider=True, text="Rot")
        op10 = row.operator("scene.rothdri", icon='FILE_REFRESH')
        row = layout.row()
        row.label(text="Mode:")
        row = layout.row()
        op3 = row.operator("scene.preview",text='Work', icon='SHADING_TEXTURE')
        op3.var3 = "MATERIAL"
        op3 = row.operator("scene.preview",text='Preview', icon='SHADING_RENDERED')
        op3.var3 = "RENDERED"
        row = layout.row()
        row.operator("scene.cam",text='Camera View', icon='OUTLINER_OB_CAMERA')
        
        row = layout.row()
        
        row.label(text="Resolution:")
        row = layout.row()
        op1 = row.operator("scene.resolution", text='270')
        op1.var1 = 25
        op1 = row.operator("scene.resolution", text='540')
        op1.var1 = 50
        op1 = row.operator("scene.resolution", text='1080')
        op1.var1 = 100
        
        row = layout.row()
        row.label(text="Quality:")
        row = layout.row()
        op2 = row.operator("scene.qualitat", text='low')
        op2.var2 = 5
        op2 = row.operator("scene.qualitat", text='middle')
        op2.var2 = 100
        op2 = row.operator("scene.qualitat", text='high')
        op2.var2 = 500
        row = layout.row()
        scene = context.scene
        rd = scene.render

        layout.prop(rd, "film_transparent", text="Transparent")
        row = layout.row()
        row.operator("render.render", text="Render", icon='RENDER_STILL')
        row = layout.row()
           
        row.operator("scene.folder", icon='FILEBROWSER')

        #row = layout.row()
        #row.operator("scene.resetstartupfile", icon='FILE_REFRESH')

        row = layout.row()
        row.operator("scene.instruction", icon='HELP')

        row = layout.row()
        
        row.label(text="pandartb3d")
         
def register() :
    bpy.utils.register_class(panel) 
    bpy.utils.register_class(ResetStartupFile)
    bpy.utils.register_class(Instruction)
    bpy.utils.register_class(ImportObj)
    bpy.utils.register_class(SaveFile)
    bpy.utils.register_class(Resolution)
    bpy.utils.register_class(Qualitat)
    bpy.utils.register_class(Preview)
    bpy.utils.register_class(Smooth)
    bpy.utils.register_class(SelectAll)
    bpy.utils.register_class(Cam)
    bpy.utils.register_class(Folder)
    bpy.utils.register_class(ChangeHDRI)
    bpy.utils.register_class(ReplaceMaterial)
    bpy.utils.register_class(Materials)
    bpy.utils.register_class(RotHDRI)



def unregister() :
    bpy.utils.unregister_class(panel)  
    bpy.utils.unregister_class(ResetStartupFile)
    bpy.utils.unregister_class(Instruction)
    bpy.utils.unregister_class(ImportObj)
    bpy.utils.unregister_class(SaveFile)
    bpy.utils.unregister_class(Resolution)
    bpy.utils.unregister_class(Qualitat)
    bpy.utils.unregister_class(Preview)
    bpy.utils.unregister_class(Smooth)
    bpy.utils.unregister_class(SelectAll)
    bpy.utils.unregister_class(Cam)
    bpy.utils.unregister_class(Folder)
    bpy.utils.unregister_class(ChangeHDRI)
    bpy.utils.unregister_class(ReplaceMaterial)
    bpy.utils.unregister_class(Materials)
    bpy.utils.unregister_class(RotHDRI)

  
 
if __name__ == "__main__" :
    register()
