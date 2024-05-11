from typing import Set
import bpy
from bpy.types import Context
 
bl_info = {
 "name": "Godot import hints",
 "description": "easier export options for Godot",
 "author": "Tester",
 "blender": (4, 0, 0),
 "version": (0, 1, 0),
 "category": "Q.O.L",
}

#this is a test
class __PT__GodotSuffix(bpy.types.Panel):
    bl_idname = "OBJECT__PT__GodotSuffix"
    bl_label = "Godot import hints"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Godot import hints"
    bl_context = "objectmode"

 
    def draw(self, context):
        layout = self.layout
        
        row = layout.row(); row.operator("object.collidersuffix")

        row2 = layout.row(); row2.operator("object.convcolcollidersuffix")

        row3 = layout.row(); row3.operator("object.rigidbodysuffix")

        row4 = layout.row(); row4.operator("object.noimportsuffix")

#this is there class that the suffix apliers deviate from, since they might need differnet functionality. 
#doens't call the bpy.types.Operator cause that make it go broken, you don't need it for a an operator.
#to make operators they need to start with Object.
#and they need a idname that follow the convention Object.instertname 
# will add a appending method for better suffix support 
# you can only pass self and context in to execute so it needs a class variable for the suffix 
#children must run the super.execute to end their task .
class ObjectSuffixTemplate(bpy.types.Operator):
    bl_idname = "object.suffixTemplate" # id name that blender uses to identify
    bl_label = "Suffix template"        # name of the operator
    bl_options = {'REGISTER', 'UNDO'}   # Enable undo for the operator.

    suffix:str

    def __init__(self) -> None:
        pass

    def execute(self, context: Context) -> Set[str] | Set[int]:

        return {"FINISHED"}
    
    def append_suffix(self, name:str):
        print("rtest")
        if self.suffix in name: #this removes it if it already there
            temp:tuple = name.rpartition(self.suffix)
            return temp[0] + temp[2]
        else:# adds if not yet there 
            return name + self.suffix 


class ObjectColliderSuffix(ObjectSuffixTemplate):
    bl_idname = "object.collidersuffix"
    bl_label = "Colision"

    suffix = "-col"

    def execute(self, context: Context) -> Set[str] | Set[int]:
        context.active_object.name = self.append_suffix(context.active_object.name)
        return super().execute(context)
    pass

class ObjectRigidbodySuffix(ObjectSuffixTemplate):
    bl_idname = "object.rigidbodysuffix"
    bl_label = "Rigidbody"

    suffix = "-rigid"

    def execute(self, context: Context) -> Set[str] | Set[int]:
        context.active_object.name = self.append_suffix(context.active_object.name)
        return super().execute(context)

class ObjectConvcolColliderSuffix(ObjectSuffixTemplate):
    bl_idname = "object.convcolcollidersuffix"
    bl_label = "Optimised Collider"

    suffix = "-convcol"

    def execute(self, context: Context) -> Set[str] | Set[int]:
        context.active_object.name = self.append_suffix(context.active_object.name)
        return super().execute(context)

class ObjectNoImportSuffix(ObjectSuffixTemplate):
    bl_idname = "object.noimportsuffix"
    bl_label = "No import"

    suffix = "-noimp"

    def execute(self, context: Context) -> Set[str] | Set[int]:
        context.active_object.name = self.append_suffix(context.active_object.name)
        return super().execute(context)


def register():
    bpy.utils.register_class(__PT__GodotSuffix)
    bpy.utils.register_class(ObjectColliderSuffix)
    bpy.utils.register_class(ObjectRigidbodySuffix)
    bpy.utils.register_class(ObjectConvcolColliderSuffix)
    bpy.utils.register_class(ObjectNoImportSuffix)
 
def unregister():
    bpy.utils.unregister_class(__PT__GodotSuffix)
    bpy.utils.unregister_class(ObjectColliderSuffix)
    bpy.utils.unregister_class(ObjectRigidbodySuffix)
    bpy.utils.unregister_class(ObjectConvcolColliderSuffix)
    bpy.utils.unregister_class(ObjectNoImportSuffix)

if __name__ == "__main__":
    register()

