"""
Copyright (C) 2016-2024 Andreas Esau and Tyler Walker
andreasesau@gmail.com, tyler@beyondstudios.us

Created by Andreas Esau modified by Tyler Walker

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

bl_info = {
    "name": "Driver to Bone Constraint",
    "description": "This Operator lets you create a shape driver constraint to a bone with one single dialog operator. Quick and easy.",
    "author": "Tyler Walker (Beyond Dev)",
    "version": (2, 0, 0, "Beta"),
    "blender": (2, 80, 0),
    "location": "Operator Search -> Driver Constraint",
    "warning": "This addon is still in development.",
    "wiki_url": "https://github.com/ndee85/Driver-Constraint-Addon",
    "category": "Rigging",
}


import bpy


# load and reload submodules
##################################

import importlib
from . import developer_utils

importlib.reload(developer_utils)
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())


# register
##################################

import traceback


def add_to_specials(self, context):
    if len(bpy.context.selected_objects) > 0:
        self.layout.operator_context = "INVOKE_DEFAULT"
        self.layout.separator()
        op = self.layout.operator(
            "object.create_driver_constraint", text="Driver Constraint", icon="DRIVER"
        )
        op.mode = "DRIVER"
        if context.active_object.type == "ARMATURE":
            try:
                if len(context.selected_pose_bones) > 1:
                    op = self.layout.operator(
                        "object.create_driver_constraint",
                        text="Action Constraint",
                        icon="ACTION",
                    )
                    op.mode = "ACTION"
            except:
                pass


def add_pose_tools(self, context):
    if len(bpy.context.selected_objects) > 0:
        self.layout.operator_context = "INVOKE_DEFAULT"
        self.layout.separator()
        self.layout.label(text="Driver Tools:")
        op = self.layout.operator(
            "object.create_driver_constraint", text="Driver Constraint", icon="DRIVER"
        )
        op.mode = "DRIVER"
        if context.active_object != None and context.active_object.type == "ARMATURE":
            try:
                if len(context.selected_pose_bones) > 1:
                    op = self.layout.operator(
                        "object.create_driver_constraint",
                        text="Action Constraint",
                        icon="ACTION",
                    )
                    op.mode = "ACTION"
            except:
                pass


def register():
    bpy.types.VIEW3D_MT_pose_context_menu.append(add_to_specials)
    bpy.types.VIEW3D_MT_object_context_menu.append(add_to_specials)
    bpy.types.VIEW3D_PT_tools_posemode_options.append(add_pose_tools)
    bpy.types.VIEW3D_PT_tools_active.append(add_pose_tools)

    print("Registered {} with {} modules".format(bl_info["name"], len(modules)))


def unregister():
    bpy.types.VIEW3D_MT_pose_context_menu.remove(add_to_specials)
    bpy.types.VIEW3D_MT_object_context_menu.remove(add_to_specials)
    bpy.types.VIEW3D_PT_tools_posemode_options.remove(add_pose_tools)
    bpy.types.VIEW3D_PT_tools_active.remove(add_pose_tools)

    print("Unregistered {}".format(bl_info["name"]))
