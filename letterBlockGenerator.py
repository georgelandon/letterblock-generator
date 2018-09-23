#Script to generate meshes from strings and export as FBX
#should work with any array of strings...
#Tested with Maya 2015
#Author: George Landon - 3/8/15
#http://www.georgelandon.com
import maya.cmds as cmds
import maya.mel as mm


#A FBX File will be created for each one of these characters
letter_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];#, '=', '+', '-', '!', '?', '.', ','];

#All FBX files will be created in this location
path = 'C:/temp/';

color_array = ['redPaint', 'greenPaint', 'bluePaint', 'yellowPaint'];
c1 = [94,33,59];
c2 = [110,73,39];
c3 = [24,62,67];
c4 = [72,101,35];
cW = [169, 145, 123];

#Palette
#https://coolors.co/792435-489d73-c93634-d47531-eac55e

#Create each material
mm.eval('shadingNode -asShader lambert -n wood');
mm.eval('sets -renderable true -noSurfaceShader true -empty -name woodSG');
mm.eval('connectAttr -f wood.outColor woodSG.surfaceShader');
mm.eval('setAttr wood.color -type double3 '+ str(cW[0]/255.0) + ' ' +str(cW[1]/255.0) + ' ' +str(cW[2]/255.0));

mm.eval('shadingNode -asShader lambert -n '+str(color_array[0]));
mm.eval('sets -renderable true -noSurfaceShader true -empty -name '+str(color_array[0])+'SG');
mm.eval('connectAttr -f '+str(color_array[0])+'.outColor '+str(color_array[0])+'SG.surfaceShader');
mm.eval('setAttr '+str(color_array[0])+'.color -type double3 '+ str(c1[0]/255.0) + ' ' +str(c1[1]/255.0) + ' ' +str(c1[2]/255.0));

mm.eval('shadingNode -asShader lambert -n '+str(color_array[1]));
mm.eval('sets -renderable true -noSurfaceShader true -empty -name '+str(color_array[1])+'SG');
mm.eval('connectAttr -f '+str(color_array[1])+'.outColor '+str(color_array[1])+'SG.surfaceShader');
mm.eval('setAttr '+str(color_array[1])+'.color -type double3 '+ str(c2[0]/255.0) + ' ' +str(c2[1]/255.0) + ' ' +str(c2[2]/255.0));

mm.eval('shadingNode -asShader lambert -n '+str(color_array[2]));
mm.eval('sets -renderable true -noSurfaceShader true -empty -name '+str(color_array[2])+'SG');
mm.eval('connectAttr -f '+str(color_array[2])+'.outColor '+str(color_array[2])+'SG.surfaceShader');
mm.eval('setAttr '+str(color_array[2])+'.color -type double3 '+ str(c3[0]/255.0) + ' ' +str(c3[1]/255.0) + ' ' +str(c3[2]/255.0));

mm.eval('shadingNode -asShader lambert -n '+str(color_array[3]));
mm.eval('sets -renderable true -noSurfaceShader true -empty -name '+str(color_array[3])+'SG');
mm.eval('connectAttr -f '+str(color_array[3])+'.outColor '+str(color_array[3])+'SG.surfaceShader');
mm.eval('setAttr '+str(color_array[3])+'.color -type double3 '+ str(c4[0]/255.0) + ' ' +str(c4[1]/255.0) + ' ' +str(c4[2]/255.0));



for i in range(len(letter_array)):
    
    #Generate the Letter Mesh (Using Tahoma Font)
    mm.eval('createNode makeTextCurves -n "textForBevel' + str(letter_array[i]) + '"');
    mm.eval('setAttr -type "string" textForBevel' + str(letter_array[i]) + '.text ' + str(letter_array[i]));
    mm.eval('setAttr -type "string" textForBevel' + str(letter_array[i]) + '.font "Segoe WP|w700|h-11"');
    
    mm.eval('createNode bevelPlus -n bevel' + str(letter_array[i]));
    mm.eval('createNode styleCurve -n innerStyleCurve' + str(letter_array[i]));
    mm.eval('createNode styleCurve -n outerStyleCurve' + str(letter_array[i]));
    mm.eval('setAttr outerStyleCurve' + str(letter_array[i]) + '.style 0');
    mm.eval('setAttr innerStyleCurve' + str(letter_array[i]) + '.style 0');
    mm.eval('setAttr bevel' + str(letter_array[i]) + '.width 0');
    mm.eval('setAttr bevel' + str(letter_array[i]) + '.depth 0');
    mm.eval('setAttr bevel' + str(letter_array[i]) + '.extrudeDepth 0.5');
    mm.eval('setAttr bevel' + str(letter_array[i]) + '.capSides 4');
    mm.eval('setAttr bevel' + str(letter_array[i]) + '.numberOfSides 4');
    mm.eval('setAttr bevel' + str(letter_array[i]) + '.tolerance 0.01');
    mm.eval('setAttr bevel' + str(letter_array[i]) + '.bevelInside 1');
    mm.eval('setAttr bevel' + str(letter_array[i]) + '.normalsOutwards true');
    mm.eval('setAttr bevel' + str(letter_array[i]) + '.polyOutUseChordHeight false');
    mm.eval('setAttr bevel' + str(letter_array[i]) + '.polyOutUseChordHeightRatio false');
    mm.eval('setAttr bevel' + str(letter_array[i]) + '.orderedCurves true');
    mm.eval('createNode mesh -n polySurfaceShape' + str(letter_array[i]));

    mm.eval('connectAttr textForBevel' + str(letter_array[i]) + '.outputCurve bevel' + str(letter_array[i]) + '.inputCurves');
    mm.eval('connectAttr textForBevel' + str(letter_array[i]) + '.count bevel' + str(letter_array[i]) + '.count');
    mm.eval('connectAttr textForBevel' + str(letter_array[i]) + '.position bevel' + str(letter_array[i]) + '.position');
    mm.eval('connectAttr innerStyleCurve' + str(letter_array[i]) + '.outCurve bevel' + str(letter_array[i]) + '.innerStyleCurve');
    mm.eval('connectAttr outerStyleCurve' + str(letter_array[i]) + '.outCurve bevel' + str(letter_array[i]) + '.outerStyleCurve');
    mm.eval('connectAttr bevel' + str(letter_array[i]) + '.outputPoly polySurfaceShape' + str(letter_array[i]) + '.inMesh');
    mm.eval('sets -edit -forceElement initialShadingGroup polySurfaceShape' + str(letter_array[i]));

    #Reposition and delete construction history
    mm.eval('xform -cp polySurface' + str(letter_array[i]));
    XYZ = cmds.objectCenter('polySurface' + str(letter_array[i]), gl=True)
    mm.eval('setAttr polySurface' + str(letter_array[i]) + '.translateX '+ str(-XYZ[0]));
    mm.eval('setAttr polySurface' + str(letter_array[i]) + '.translateZ '+ str(-XYZ[2] - 0.25));
    mm.eval('setAttr polySurface' + str(letter_array[i]) + '.translateY '+ str(0.35));
    if letter_array[i] == '_':
        mm.eval('setAttr polySurface' + str(letter_array[i]) + '.translateY '+ str(.55));        
    cmds.makeIdentity( 'polySurface' + str(letter_array[i]), apply=True, translate=True )
    if letter_array[i] == 'W':
        mm.eval('scale -r 0.85 1.0 1.0');    
    mm.eval('scale -r 0.8 0.8 0.8');
    cmds.delete(ch=True )
    mm.eval('sets -e -forceElement '+str(color_array[i%4])+'SG');
    
    mm.eval('polyCube -ch on -o on -w 3 -h 3 -d 3 -cuv 4 -n sblock' + str(letter_array[i]));
    mm.eval('polyCube -ch on -o on -w 2.5 -h 2.5 -d 0.25 -cuv 4 -n cutout' + str(letter_array[i]));
    mm.eval('setAttr sblock' + str(letter_array[i]) + '.translateY '+ str(1.5));
    mm.eval('setAttr sblock' + str(letter_array[i]) + '.translateZ '+ str(-1.5));
    mm.eval('setAttr cutout' + str(letter_array[i]) + '.translateY '+ str(1.5));
    mm.eval('polyCBoolOp -op 2 -ch 1 -preserveColor 0 -classification 2 -name block' + str(letter_array[i])+ ' sblock' + str(letter_array[i])+ ' cutout' + str(letter_array[i]) );
    mm.eval('polyBevel -com 0 -fraction 0.25 -offsetAsFraction 1 -autoFit 1 -segments 5 -worldSpace 1 -uvAssignment 0 -smoothingAngle 30 -fillNgons 1 -mergeVertices 1 -mergeVertexTolerance 0.0001 -miteringAngle 180 -angleTolerance 180 -ch 1 block'+ str(letter_array[i]) + '.e[10:11] block'+ str(letter_array[i]) + '.e[14] block'+ str(letter_array[i]) + '.e[16]');
    cmds.makeIdentity( 'block' + str(letter_array[i]), apply=True, translate=True )
    cmds.delete(ch=True )
    

    mm.eval('select -r block'+ str(letter_array[i]) + '.f[0] block'+ str(letter_array[i]) + '.f[10] block'+ str(letter_array[i]) + '.f[42:46] block'+ str(letter_array[i]) + '.f[38] block'+ str(letter_array[i]) + '.f[32:36] block'+ str(letter_array[i]) + '.f[40]');

    mm.eval('sets -e -forceElement '+str(color_array[i%4])+'SG');
    mm.eval('invertSelection');
    mm.eval('sets -e -forceElement woodSG');
    mm.eval('polyTriangulate -ch 1 block'+ str(letter_array[i]));
    mm.eval('polyBoolOp -op 1 -ch 1 -useThresholds 1 -preserveColor 0 -name LetterBlock'+ str(letter_array[i])+' block'+ str(letter_array[i]) + ' polySurface' + str(letter_array[i]) );
    mm.eval('polySetToFaceNormal');
    cmds.delete(ch=True )    
    
    #prep FBX export   
    mm.eval("FBXExportSmoothingGroups -v false")
    mm.eval("FBXExportHardEdges -v false")
    mm.eval("FBXExportTangents -v false")
    mm.eval("FBXExportSmoothMesh -v false")
    mm.eval("FBXExportInstances -v false")

    mm.eval("FBXExportBakeComplexAnimation -v false")
   
    mm.eval("FBXExportUseSceneName -v false")
    mm.eval("FBXExportQuaternion -v euler")
    mm.eval("FBXExportShapes -v true")
    mm.eval("FBXExportSkins -v true")

    mm.eval("FBXExportConstraints -v false")
    mm.eval("FBXExportCameras -v false")
    mm.eval("FBXExportLights -v false")
    mm.eval("FBXExportEmbeddedTextures -v false")
    mm.eval("FBXExportInputConnections -v false")
    
    #Axis
    mm.eval("FBXExportUpAxis y")

    # Export to FBX
    mm.eval('FBXExport -f "' + path + str(letter_array[i]) + '.fbx" -s')
    print 'finished exporting letter: ', str(letter_array[i]);