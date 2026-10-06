import os.path
import numpy as np
import pyglet
import pyglet.gl as GL
from pathlib import Path
import grafica.transformations as tr
from grafica.scenegraph import Scenegraph

pose_actual=0

def tarea():

 vertex_source = """#version 330 core
 in vec3 position;

 uniform mat4 transform;
 uniform mat4 view;
 uniform mat4 projection;

 void main() {
    gl_Position = projection * view * transform * vec4(position, 1.0);

 }

 """



 fragment_source = """#version 330 core
 uniform vec3 color;
 out vec4 fragColor;

 void main() {
    fragColor = vec4(color, 1.0);
 }

 """



 pose_actual = 0


 window = pyglet.window.Window(width=800, height=800, caption="Personaje articulado y poses dramáticas")
 vert_shader = pyglet.graphics.shader.Shader(vertex_source, "vertex")
 frag_shader = pyglet.graphics.shader.Shader(fragment_source, "fragment")
 pipeline = pyglet.graphics.shader.ShaderProgram(vert_shader, frag_shader)


 grafo = Scenegraph("personaje")
 grafo.load_and_register_mesh('cube', "assets/cube.off", fix_normals=True)
 grafo.register_pipeline('basic_pipeline', pipeline)
 grafo.add_mesh_instance("base_mesh","cube","basic_pipeline",color=np.array([0.0, 0.0, 0.5],dtype=np.float32))




 grafo.add_edge("personaje", "base_pos")  
 grafo.add_edge("base_pos", "base_rotation")  
 grafo.add_edge("base_rotation", "cubo_1_scale")  
 grafo.add_edge("cubo_1_scale", "base_geometry")
 grafo.add_edge("base_geometry","base_mesh")






 grafo.load_and_register_mesh('cube_2', "assets/cube.off", fix_normals=True)
 grafo.add_mesh_instance("base_mesh_cube_2","cube_2","basic_pipeline",color=np.array([1.0,1.0,0.0],dtype=np.float32))




 grafo.add_edge("base_rotation", "cubo_2_pos")  
 grafo.add_edge("cubo_2_pos", "cubo_2_rotation")  
 grafo.add_edge("cubo_2_rotation", "cubo_2_geometry_1")
 grafo.add_edge("cubo_2_geometry_1", "cubo_2_geometry_2")
 grafo.add_edge("cubo_2_geometry_2", "base_mesh_cube_2")






 grafo.load_and_register_mesh('cube_3', "assets/cube.off", fix_normals=True)
 grafo.add_mesh_instance("base_mesh_cube_3","cube_3","basic_pipeline",color=np.array([1.0,1.0,0.0],dtype=np.float32))




 grafo.add_edge("base_rotation", "cubo_3_pos")  
 grafo.add_edge("cubo_3_pos", "cubo_3_rotation")  
 grafo.add_edge("cubo_3_rotation", "cubo_3_geometry_1")
 grafo.add_edge("cubo_3_geometry_1", "cubo_3_geometry_2")
 grafo.add_edge("cubo_3_geometry_2", "base_mesh_cube_3")







 grafo.load_and_register_mesh('cadera', "assets/cube.off", fix_normals=True)
 grafo.add_mesh_instance("base_mesh_c","cadera","basic_pipeline",color=np.array([1.0,1.0,1.0],dtype=np.float32))




 grafo.add_edge("base_rotation", "cadera_pos")
 grafo.add_edge("cadera_pos", "cadera_rotation")  
 grafo.add_edge("cadera_rotation", "cadera_scale")
 grafo.add_edge("cadera_scale", "cadera_geometry")
 grafo.add_edge("cadera_geometry", "base_mesh_c")







 grafo.load_and_register_mesh('cube_4', "assets/cube.off", fix_normals=True)
 grafo.add_mesh_instance("base_mesh_cube_4","cube_4","basic_pipeline",color=np.array([1.0,1.0,0.0],dtype=np.float32))


 grafo.add_edge("cadera_rotation", "cubo_4_pos")
 grafo.add_edge("cubo_4_pos", "cubo_4_rotation")  
 grafo.add_edge("cubo_4_rotation", "cubo_4_geometry_1")
 grafo.add_edge("cubo_4_geometry_1", "cubo_4_geometry_2")
 grafo.add_edge("cubo_4_geometry_2", "base_mesh_cube_4")







 grafo.load_and_register_mesh('cube_5', "assets/cube.off", fix_normals=True)
 grafo.add_mesh_instance("base_mesh_cube_5","cube_5","basic_pipeline",color=np.array([1.0,1.0,0.0],dtype=np.float32))



 grafo.add_edge("cadera_rotation", "cubo_5_pos") 
 grafo.add_edge("cubo_5_pos", "cubo_5_rotation")  
 grafo.add_edge("cubo_5_rotation", "cubo_5_geometry_1")
 grafo.add_edge("cubo_5_geometry_1", "cubo_5_geometry_2")
 grafo.add_edge("cubo_5_geometry_2", "base_mesh_cube_5")







 grafo.load_and_register_mesh('cube_6', "assets/sphere.off", fix_normals=True)
 grafo.add_mesh_instance("base_mesh_cube_6","cube_6","basic_pipeline",color=np.array([1.0, 0.85, 0.72],dtype=np.float32))


 grafo.add_edge("base_rotation", "cubo_6_pos")  
 grafo.add_edge("cubo_6_pos", "cubo_6_rotation")  
 grafo.add_edge("cubo_6_rotation", "cubo_6_geometry")
 grafo.add_edge("cubo_6_geometry", "base_mesh_cube_6")


 grafo.load_and_register_mesh('brazo1', "assets/cube.off", fix_normals=True)
 grafo.add_mesh_instance("base_mesh_brazo1","brazo1","basic_pipeline",color=np.array([1.0, 0.85, 0.72],dtype=np.float32))





 grafo.add_edge("cubo_2_rotation", "brazo1_rotation")  
 grafo.add_edge("brazo1_rotation", "brazo1_pos")  
 grafo.add_edge("brazo1_pos", "brazo1_geometry_1")
 grafo.add_edge("brazo1_geometry_1", "brazo1_geometry_2")
 grafo.add_edge("brazo1_geometry_2", "base_mesh_brazo1")






 grafo.load_and_register_mesh('brazo2', "assets/cube.off", fix_normals=True)
 grafo.add_mesh_instance("base_mesh_brazo2","brazo2","basic_pipeline",color=np.array([1.0, 0.85, 0.72],dtype=np.float32))



 grafo.add_edge("cubo_3_rotation", "brazo2_rotation")  
 grafo.add_edge("brazo2_rotation", "brazo2_pos")  
 grafo.add_edge("brazo2_pos", "brazo2_geometry_1")
 grafo.add_edge("brazo2_geometry_1", "brazo2_geometry_2")
 grafo.add_edge("brazo2_geometry_2", "base_mesh_brazo2")






 grafo.load_and_register_mesh('ojo1', "assets/sphere.off", fix_normals=True)
 grafo.add_mesh_instance("base_mesh_ojo1","ojo1","basic_pipeline",color=np.array([0.0,0.0,0.0],dtype=np.float32))




 grafo.add_edge("cubo_6_geometry", "eye1_pos")  
 grafo.add_edge("eye1_pos", "eye1_scale")  
 grafo.add_edge("eye1_scale", "base_mesh_ojo1")







 grafo.load_and_register_mesh('ojo2', "assets/sphere.off", fix_normals=True)
 grafo.add_mesh_instance("base_mesh_ojo2","ojo2","basic_pipeline",color=np.array([0.0,0.0,0.0],dtype=np.float32))



 grafo.add_edge("cubo_6_geometry", "eye2_pos")  
 grafo.add_edge("eye2_pos", "eye2_scale")  
 grafo.add_edge("eye2_scale", "base_mesh_ojo2")






 grafo.load_and_register_mesh('boca', "assets/cube.off", fix_normals=True)
 grafo.add_mesh_instance("base_mesh_boca","boca","basic_pipeline",color=np.array([0.0,0.0,0.0],dtype=np.float32))




 grafo.add_edge("cubo_6_geometry", "boca_pos")  
 grafo.add_edge("boca_pos", "boca_rotation")  
 grafo.add_edge("boca_rotation", "boca_scale")
 grafo.add_edge("boca_scale","boca_geometry")
 grafo.add_edge("boca_geometry","base_mesh_boca")



 gpu_data=grafo

 view_matrix = tr.lookAt(np.array([0, 0, 3]), np.array([0, 0, 0]), np.array([0, 1, 0]))
 projection_matrix = tr.perspective(45, window.aspect_ratio, 0.1, 100.0)

 def actualizar_pose_gpu(): 
    nonlocal pose_actual
    nonlocal view_matrix
    nonlocal projection_matrix

    if pose_actual==0:

    
        grafo.add_transform("base_rotation", tr.identity())
        grafo.add_transform("cubo_1_scale", tr.scale(1.0, 1.5, 0.5))
        grafo.add_transform("base_geometry", tr.uniformScale(0.3))

        grafo.add_transform("cubo_2_pos", tr.translate(0.2, 0.1, 0.0))
        grafo.add_transform("cubo_2_rotation", tr.rotationZ(-45))
        grafo.add_transform("cubo_2_geometry_1", tr.scale(0.5, 0.2, 0.2))
        grafo.add_transform("cubo_2_geometry_2", tr.uniformScale(0.4))

        grafo.add_transform("cubo_3_pos", tr.translate(-0.2,0.1, 0.0))
        grafo.add_transform("cubo_3_rotation", tr.rotationZ(45))
        grafo.add_transform("cubo_3_geometry_1", tr.scale(0.5, 0.2, 0.2))
        grafo.add_transform("cubo_3_geometry_2", tr.uniformScale(0.4))

        grafo.add_transform("cadera_pos", tr.translate(0.0,-0.35,0.0))
        grafo.add_transform("cadera_rotation", tr.identity())
        grafo.add_transform("cadera_scale", tr.scale(1.0, 0.5, 0.5))
        grafo.add_transform("cadera_geometry", tr.uniformScale(0.3))

        grafo.add_transform("cubo_4_pos", tr.translate(-0.1,-0.2, 0.0))
        grafo.add_transform("cubo_4_rotation", tr.matmul([tr.identity(), tr.identity(), tr.identity()]))
        grafo.add_transform("cubo_4_geometry_1", tr.scale(0.2, 0.5, 0.2))
        grafo.add_transform("cubo_4_geometry_2", tr.uniformScale(0.4))

        grafo.add_transform("cubo_5_pos", tr.translate(0.1,-0.2, 0.0))
        grafo.add_transform("cubo_5_rotation", tr.matmul([tr.identity(), tr.identity(), tr.identity()]))
        grafo.add_transform("cubo_5_geometry_1", tr.scale(0.2, 0.5, 0.2))
        grafo.add_transform("cubo_5_geometry_2", tr.uniformScale(0.4))

        grafo.add_transform("cubo_6_pos", tr.translate(0.0,0.4, 0.0))
        grafo.add_transform("cubo_6_rotation", tr.identity())
        grafo.add_transform("cubo_6_geometry", tr.uniformScale(0.25))

        grafo.add_transform("brazo1_rotation", tr.rotationZ(45))
        grafo.add_transform("brazo1_pos", tr.translate(0.05,-0.2, 0.0))
        grafo.add_transform("brazo1_geometry_1", tr.scale(0.2, 0.7, 0.2))
        grafo.add_transform("brazo1_geometry_2", tr.uniformScale(0.35))

        grafo.add_transform("brazo2_rotation", tr.rotationZ(-45))
        grafo.add_transform("brazo2_pos", tr.translate(-0.05,-0.2, 0.0))
        grafo.add_transform("brazo2_geometry_1", tr.scale(0.2, 0.7, 0.2))
        grafo.add_transform("brazo2_geometry_2", tr.uniformScale(0.35))

        grafo.add_transform("eye1_pos", tr.translate(0.25,0.0,0.5))
        grafo.add_transform("eye1_scale", tr.uniformScale(0.1))

        grafo.add_transform("eye2_pos", tr.translate(-0.25,0.0,0.5))
        grafo.add_transform("eye2_scale", tr.uniformScale(0.1))

        grafo.add_transform("boca_pos", tr.translate(0.0,-0.41,0.4))
        grafo.add_transform("boca_rotation", tr.identity())
        grafo.add_transform("boca_scale", tr.scale(1.2,0.2,0.2))
        grafo.add_transform("boca_geometry", tr.uniformScale(0.3))


        view_matrix = tr.lookAt(np.array([0, 0, 2]), np.array([0, 0, 0]), np.array([0, 1, 0]))
        projection_matrix = tr.perspective(45, window.aspect_ratio, 0.1, 100.0)

       

    elif pose_actual==1:


        grafo.add_transform("cadera_rotation", tr.matmul([tr.rotationX(45), tr.rotationY(0), tr.identity()]))
        grafo.add_transform("cubo_5_rotation", tr.matmul([tr.rotationX(0), tr.rotationY(-50), tr.identity()]))
        grafo.add_transform("cubo_4_rotation", tr.matmul([tr.rotationX(0), tr.rotationY(50), tr.identity()]))
        grafo.add_transform("cubo_2_rotation", tr.matmul([tr.rotationX(-15), tr.identity(), tr.identity()]))
        grafo.add_transform("cubo_3_rotation", tr.matmul([tr.rotationX(-15), tr.identity(), tr.identity()]))
        grafo.add_transform("cubo_6_rotation", tr.matmul([tr.rotationX(-25), tr.identity(), tr.identity()]))

        view_matrix=tr.lookAt(np.array([0, -1, 1]), np.array([0.0, 1, 0.0]), np.array([0.0, 1.0, 0.0]))
        projection_matrix = tr.perspective(90, window.aspect_ratio, 0.1, 100.0)

       

    elif pose_actual==2:

       
        grafo.add_transform("base_rotation", tr.matmul([tr.rotationX(0), tr.rotationY(18.5), tr.identity()]))
        grafo.add_transform("cadera_rotation", tr.matmul([tr.rotationX(0), tr.rotationY(-30), tr.identity()]))
        grafo.add_transform("cubo_2_rotation", tr.matmul([tr.rotationX(0), tr.rotationY(0), tr.rotationZ(-45)]))
        grafo.add_transform("cubo_3_rotation", tr.matmul([tr.rotationX(0), tr.rotationY(0), tr.rotationZ(30)]))
        grafo.add_transform("cubo_3_pos", tr.translate(-0.25,0.2,0.0))
        grafo.add_transform("cubo_6_rotation", tr.matmul([tr.rotationX(5.4), tr.rotationY(5.4), tr.rotationZ(-0.7)]))
        grafo.add_transform("brazo2_rotation", tr.matmul([tr.rotationX(0), tr.rotationY(0), tr.rotationZ(30)]))
        grafo.add_transform("brazo2_pos", tr.translate(0.0,-0.25,0.0))

        view_matrix=tr.lookAt(np.array([-8.0, 8.0, 3]), np.array([0.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]))
        projection_matrix=tr.perspective(20, window.aspect_ratio, 0.1, 100.0)



    elif pose_actual==3:

        grafo.add_transform("cubo_3_pos",tr.translate(-0.2, 0.1, 0.0))
        grafo.add_transform("brazo2_pos",tr.translate(-0.05, -0.2, 0.0))
        grafo.add_transform("base_rotation", tr.matmul([tr.rotationX(-15),tr.rotationY(0),tr.identity()]))
        grafo.add_transform("cadera_rotation",tr.matmul([tr.rotationX(20),tr.rotationY(0),tr.rotationZ(0)])) 
        grafo.add_transform("cubo_2_rotation",tr.matmul([tr.rotationX(0),tr.rotationY(0),tr.rotationZ(120)]))
        grafo.add_transform("cubo_3_rotation",tr.matmul([tr.rotationX(0),tr.rotationY(0),tr.rotationZ(-120)]))

        grafo.add_transform("brazo1_rotation",tr.matmul([tr.rotationX(0),tr.rotationY(0),tr.rotationZ(20)]))
        grafo.add_transform("brazo2_rotation",tr.matmul([tr.rotationX(0),tr.rotationY(0),tr.rotationZ(-20)]))

        grafo.add_transform("cubo_4_rotation",tr.matmul([tr.rotationX(0),tr.rotationY(0),tr.rotationZ(-35)]))
        grafo.add_transform("cubo_5_rotation",tr.matmul([tr.rotationX(0),tr.rotationY(0),tr.rotationZ(35)]))
        grafo.add_transform("cubo_6_rotation",tr.matmul([tr.rotationX(0),tr.rotationY(90),tr.identity()]))

        view_matrix=tr.lookAt(np.array([2.0, -3.0, 1.0]),np.array([0.0, 0.0, 0.0]),np.array([1.0, 1.0, 0.0]))
        projection_matrix=tr.perspective(30, window.aspect_ratio, 0.1,100.0)

 actualizar_pose_gpu()



 @window.event
 def on_key_press(symbol, modifiers):
    nonlocal pose_actual
    if symbol==pyglet.window.key.SPACE:
        pose_actual=(pose_actual + 1) % 4
        actualizar_pose_gpu()


 @window.event
 def on_draw():
    GL.glClearColor(0.2, 0.2, 0.2, 1.0)
    window.clear()
    GL.glEnable(GL.GL_DEPTH_TEST)

    if gpu_data is not None:

        gpu_data.register_view_transform(view_matrix)
        gpu_data.set_global_attributes(projection=projection_matrix)
        gpu_data.render()

 pyglet.app.run()
