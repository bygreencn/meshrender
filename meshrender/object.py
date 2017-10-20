import numpy as np

from trimesh import Trimesh
from autolab_core import RigidTransform

from .material import MaterialProperties

class SceneObject(object):
    """A complete description of an object in a Scene.

    This includes its geometry (represented as a Trimesh), its pose in the world,
    and its material properties.
    """

    def __init__(self, mesh,
                 T_obj_world=RigidTransform(from_frame='obj', to_frame='world'),
                 material=MaterialProperties()):
        """Initialize a scene object with the given mesh, pose, and material.

        Parameters
        ----------
        mesh : trimesh.Trimesh
            A mesh representing the object's geometry.
        T_obj_world : autolab_core.RigidTransform
            A rigid transformation from the object's frame to the world frame.
        material : MaterialProperties
            A set of material properties for the object.
        """
        if not isinstance(mesh, Trimesh):
            raise ValueError('mesh must be an object of type Trimesh')
        if not isinstance(material, MaterialProperties):
            raise ValueError('material must be an object of type MaterialProperties')

        if material.smooth:
            mesh = mesh.smoothed()

        self._mesh = mesh
        self._material = material
        self.T_obj_world = T_obj_world

    @property
    def mesh(self):
        """trimesh.Trimesh: A mesh representing the object's geometry.
        """
        return self._mesh

    @property
    def material(self):
        """MaterialProperties: A set of material properties for the object.
        """
        return self._material

    @property
    def T_obj_world(self):
        """autolab_core.RigidTransform: A rigid transformation from the object's frame to the world frame.
        """
        return self._T_obj_world

    @T_obj_world.setter
    def T_obj_world(self, T):
        if not isinstance(T, RigidTransform):
            raise ValueError('transform must be an object of type RigidTransform')
        if not T.from_frame == 'obj' or not T.to_frame == 'world':
            raise ValueError('transform must be from obj -> world, got {} -> {}'.format(T.from_frame, T.to_frame))
        self._T_obj_world = T

