import maya.cmds as mc

#mc.polySphere(name = 'snowman_bottom', subdivisionsHeight=20,subdivisionsAxis=32)

mc.polySphere(name='bottom',
              radius=1,
              subdivisionsX=20,
              subdivisionsY=20,
              axis=[0,1,0],
              createUVs=2,
              constructionHistory=1)

mc.move(0, 0.925293, 0, r=True, os=True, wd=True)
mc.scale(2,2,2, r=True)


mc.polySphere(name='middle',
              radius=1,
              subdivisionsX=20,
              subdivisionsY=20,
              axis=[0,1,0],
              createUVs=2,
              constructionHistory=1)

mc.select('middle')
mc.move(0, 3.5, 0, r=True, os=True, wd=True)
mc.scale(1.3,1.3,1.3, r=True)

mc.polySphere(name='top',
              radius=1,
              subdivisionsX=20,
              subdivisionsY=20,
              axis=[0,1,0],
              createUVs=2,
              constructionHistory=1)

mc.move(0, 5, 0, r=True, os=True, wd=True)
mc.scale(0.8,0.8,0.8, r=True)

mc.polyCylinder(name='arm',
                radius=0.1,
                height=2,
                subdivisionsX=20,
                subdivisionsY=1,
                subdivisionsZ=1,
                axis=[0,1,0],
                createUVs=3,
                constructionHistory=1)

mc.move(1.5, 3.5, 0, r=True, os=True, wd=True)
mc.rotate(0,0,90,r=True,os=True,ws=True)

mc.polyCylinder(name='arm',
                radius=0.1,
                height=2,
                subdivisionsX=20,
                subdivisionsY=1,
                subdivisionsZ=1,
                axis=[0,1,0],
                createUVs=3,
                constructionHistory=1)
mc.move(-1.5, 3.5, 0, r=True, os=True, wd=True)
mc.rotate(0,0,90,r=True,os=True,ws=True)