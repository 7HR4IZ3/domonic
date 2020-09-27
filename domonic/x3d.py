"""
    domonic.x3d
    ====================================
    Generate x3d with python 3

"""

from domonic.html import tag, closed_tag
from domonic.dom import Node, ParentNode


def x3dom_init(self, *args, **kwargs):
    tag.__init__(self, *args, **kwargs)
    Node.__init__(self, *args, **kwargs)


x3d = X3D = type('x3d', (tag, Node, ParentNode), {'name': 'x3d', '__init__': x3dom_init})
scene = Scene = type('scene', (tag, Node, ParentNode), {'name': 'scene', '__init__': x3dom_init})
material = Material = type('material', (tag, Node, ParentNode), {'name': 'material', '__init__': x3dom_init})
appearance = Appearance = type('appearance', (tag, Node, ParentNode), {'name': 'appearance', '__init__': x3dom_init})
sphere = Sphere = type('sphere', (tag, Node, ParentNode), {'name': 'sphere', '__init__': x3dom_init})
shape = Shape = type('shape', (tag, Node, ParentNode), {'name': 'shape', '__init__': x3dom_init})
transform = Transform = type('transform', (tag, Node, ParentNode), {'name': 'transform', '__init__': x3dom_init})
timeSensor = TimeSensor = type('timeSensor', (tag, Node, ParentNode), {'name': 'timeSensor', '__init__': x3dom_init})
inline = Inline = type('inline', (tag, Node, ParentNode), {'name': 'inline', '__init__': x3dom_init})
box = Box = type('box', (tag, Node, ParentNode), {'name': 'box', '__init__': x3dom_init})
plane = Plane = type('plane', (tag, Node, ParentNode), {'name': 'plane', '__init__': x3dom_init})

# TODO - go through examples to find which are usually lower. i.e before they allowed mised cases
positionInterpolator = PositionInterpolator = type('PositionInterpolator', (tag, Node, ParentNode), {'name': 'PositionInterpolator', '__init__': x3dom_init})
route = Route = type('Route', (tag, Node, ParentNode), {'name': 'Route', '__init__': x3dom_init})
anchor = Anchor = type('Anchor', (tag, Node, ParentNode), {'name': 'Anchor', '__init__': x3dom_init})
arc2D = Arc2D = type('Arc2D', (tag, Node, ParentNode), {'name': 'Arc2D', '__init__': x3dom_init})
arcClose2D = ArcClose2D = type('ArcClose2D', (tag, Node, ParentNode), {'name': 'ArcClose2D', '__init__': x3dom_init})
audioClip = AudioClip = type('AudioClip', (tag, Node, ParentNode), {'name': 'AudioClip', '__init__': x3dom_init})
background = Background = type('Background', (tag, Node, ParentNode), {'name': 'Background', '__init__': x3dom_init})
ballJoint = BallJoint = type('BallJoint', (tag, Node, ParentNode), {'name': 'BallJoint', '__init__': x3dom_init})
billboard = Billboard = type('Billboard', (tag, Node, ParentNode), {'name': 'Billboard', '__init__': x3dom_init})
binaryGeometry = BinaryGeometry = type('BinaryGeometry', (tag, Node, ParentNode), {'name': 'BinaryGeometry', '__init__': x3dom_init})
blendedVolumeStyle = BlendedVolumeStyle = type('BlendedVolumeStyle', (tag, Node, ParentNode), {'name': 'BlendedVolumeStyle', '__init__': x3dom_init})
blendMode = BlendMode = type('BlendMode', (tag, Node, ParentNode), {'name': 'BlendMode', '__init__': x3dom_init})
block = Block = type('Block', (tag, Node, ParentNode), {'name': 'Block', '__init__': x3dom_init})
boundaryEnhancementVolumeStyle = BoundaryEnhancementVolumeStyle = type('BoundaryEnhancementVolumeStyle', (tag, Node, ParentNode), {'name': 'BoundaryEnhancementVolumeStyle', '__init__': x3dom_init})
bufferAccessor = BufferAccessor = type('BufferAccessor', (tag, Node, ParentNode), {'name': 'BufferAccessor', '__init__': x3dom_init})
bufferGeometry = BufferGeometry = type('BufferGeometry', (tag, Node, ParentNode), {'name': 'BufferGeometry', '__init__': x3dom_init})
bufferView = BufferView = type('BufferView', (tag, Node, ParentNode), {'name': 'BufferView', '__init__': x3dom_init})
cADAssembly = CADAssembly = type('CADAssembly', (tag, Node, ParentNode), {'name': 'CADAssembly', '__init__': x3dom_init})
cADFace = CADFace = type('CADFace', (tag, Node, ParentNode), {'name': 'CADFace', '__init__': x3dom_init})
cADLayer = CADLayer = type('CADLayer', (tag, Node, ParentNode), {'name': 'CADLayer', '__init__': x3dom_init})
cADPart = CADPart = type('CADPart', (tag, Node, ParentNode), {'name': 'CADPart', '__init__': x3dom_init})
cartoonVolumeStyle = CartoonVolumeStyle = type('CartoonVolumeStyle', (tag, Node, ParentNode), {'name': 'CartoonVolumeStyle', '__init__': x3dom_init})
circle2D = Circle2D = type('Circle2D', (tag, Node, ParentNode), {'name': 'Circle2D', '__init__': x3dom_init})
clipPlane = ClipPlane = type('ClipPlane', (tag, Node, ParentNode), {'name': 'ClipPlane', '__init__': x3dom_init})
collidableShape = CollidableShape = type('CollidableShape', (tag, Node, ParentNode), {'name': 'CollidableShape', '__init__': x3dom_init})
collision = Collision = type('Collision', (tag, Node, ParentNode), {'name': 'Collision', '__init__': x3dom_init})
collisionCollection = CollisionCollection = type('CollisionCollection', (tag, Node, ParentNode), {'name': 'CollisionCollection', '__init__': x3dom_init})
collisionSensor = CollisionSensor = type('CollisionSensor', (tag, Node, ParentNode), {'name': 'CollisionSensor', '__init__': x3dom_init})
color = Color = type('Color', (tag, Node, ParentNode), {'name': 'Color', '__init__': x3dom_init})
colorChaser = ColorChaser = type('ColorChaser', (tag, Node, ParentNode), {'name': 'ColorChaser', '__init__': x3dom_init})
colorDamper = ColorDamper = type('ColorDamper', (tag, Node, ParentNode), {'name': 'ColorDamper', '__init__': x3dom_init})
colorInterpolator = ColorInterpolator = type('ColorInterpolator', (tag, Node, ParentNode), {'name': 'ColorInterpolator', '__init__': x3dom_init})
colorMaskMode = ColorMaskMode = type('ColorMaskMode', (tag, Node, ParentNode), {'name': 'ColorMaskMode', '__init__': x3dom_init})
colorRGBA = ColorRGBA = type('ColorRGBA', (tag, Node, ParentNode), {'name': 'ColorRGBA', '__init__': x3dom_init})
commonSurfaceShader = CommonSurfaceShader = type('CommonSurfaceShader', (tag, Node, ParentNode), {'name': 'CommonSurfaceShader', '__init__': x3dom_init})
composedCubeMapTexture = ComposedCubeMapTexture = type('ComposedCubeMapTexture', (tag, Node, ParentNode), {'name': 'ComposedCubeMapTexture', '__init__': x3dom_init})
composedShader = ComposedShader = type('ComposedShader', (tag, Node, ParentNode), {'name': 'ComposedShader', '__init__': x3dom_init})
composedTexture3D = ComposedTexture3D = type('ComposedTexture3D', (tag, Node, ParentNode), {'name': 'ComposedTexture3D', '__init__': x3dom_init})
composedVolumeStyle = ComposedVolumeStyle = type('ComposedVolumeStyle', (tag, Node, ParentNode), {'name': 'ComposedVolumeStyle', '__init__': x3dom_init})
cone = Cone = type('Cone', (tag, Node, ParentNode), {'name': 'Cone', '__init__': x3dom_init})
coordinate = Coordinate = type('Coordinate', (tag, Node, ParentNode), {'name': 'Coordinate', '__init__': x3dom_init})
coordinateDamper = CoordinateDamper = type('CoordinateDamper', (tag, Node, ParentNode), {'name': 'CoordinateDamper', '__init__': x3dom_init})
coordinateDouble = CoordinateDouble = type('CoordinateDouble', (tag, Node, ParentNode), {'name': 'CoordinateDouble', '__init__': x3dom_init})
coordinateInterpolator = CoordinateInterpolator = type('CoordinateInterpolator', (tag, Node, ParentNode), {'name': 'CoordinateInterpolator', '__init__': x3dom_init})
cylinder = Cylinder = type('Cylinder', (tag, Node, ParentNode), {'name': 'Cylinder', '__init__': x3dom_init})
cylinderSensor = CylinderSensor = type('CylinderSensor', (tag, Node, ParentNode), {'name': 'CylinderSensor', '__init__': x3dom_init})
depthMode = DepthMode = type('DepthMode', (tag, Node, ParentNode), {'name': 'DepthMode', '__init__': x3dom_init})
directionalLight = DirectionalLight = type('DirectionalLight', (tag, Node, ParentNode), {'name': 'DirectionalLight', '__init__': x3dom_init})
dish = Dish = type('Dish', (tag, Node, ParentNode), {'name': 'Dish', '__init__': x3dom_init})
disk2D = Disk2D = type('Disk2D', (tag, Node, ParentNode), {'name': 'Disk2D', '__init__': x3dom_init})
doubleAxisHingeJoint = DoubleAxisHingeJoint = type('DoubleAxisHingeJoint', (tag, Node, ParentNode), {'name': 'DoubleAxisHingeJoint', '__init__': x3dom_init})
dynamicLOD = DynamicLOD = type('DynamicLOD', (tag, Node, ParentNode), {'name': 'DynamicLOD', '__init__': x3dom_init})
edgeEnhancementVolumeStyle = EdgeEnhancementVolumeStyle = type('EdgeEnhancementVolumeStyle', (tag, Node, ParentNode), {'name': 'EdgeEnhancementVolumeStyle', '__init__': x3dom_init})
elevationGrid = ElevationGrid = type('ElevationGrid', (tag, Node, ParentNode), {'name': 'ElevationGrid', '__init__': x3dom_init})
environment = Environment = type('Environment', (tag, Node, ParentNode), {'name': 'Environment', '__init__': x3dom_init})
extrusion = Extrusion = type('Extrusion', (tag, Node, ParentNode), {'name': 'Extrusion', '__init__': x3dom_init})
field = Field = type('Field', (tag, Node, ParentNode), {'name': 'Field', '__init__': x3dom_init})
floatVertexAttribute = FloatVertexAttribute = type('FloatVertexAttribute', (tag, Node, ParentNode), {'name': 'FloatVertexAttribute', '__init__': x3dom_init})
fog = Fog = type('Fog', (tag, Node, ParentNode), {'name': 'Fog', '__init__': x3dom_init})
fontStyle = FontStyle = type('FontStyle', (tag, Node, ParentNode), {'name': 'FontStyle', '__init__': x3dom_init})
generatedCubeMapTexture = GeneratedCubeMapTexture = type('GeneratedCubeMapTexture', (tag, Node, ParentNode), {'name': 'GeneratedCubeMapTexture', '__init__': x3dom_init})
geoCoordinate = GeoCoordinate = type('GeoCoordinate', (tag, Node, ParentNode), {'name': 'GeoCoordinate', '__init__': x3dom_init})
geoElevationGrid = GeoElevationGrid = type('GeoElevationGrid', (tag, Node, ParentNode), {'name': 'GeoElevationGrid', '__init__': x3dom_init})
geoLocation = GeoLocation = type('GeoLocation', (tag, Node, ParentNode), {'name': 'GeoLocation', '__init__': x3dom_init})
geoLOD = GeoLOD = type('GeoLOD', (tag, Node, ParentNode), {'name': 'GeoLOD', '__init__': x3dom_init})
geoMetadata = GeoMetadata = type('GeoMetadata', (tag, Node, ParentNode), {'name': 'GeoMetadata', '__init__': x3dom_init})
geoOrigin = GeoOrigin = type('GeoOrigin', (tag, Node, ParentNode), {'name': 'GeoOrigin', '__init__': x3dom_init})
geoPositionInterpolator = GeoPositionInterpolator = type('GeoPositionInterpolator', (tag, Node, ParentNode), {'name': 'GeoPositionInterpolator', '__init__': x3dom_init})
geoTransform = GeoTransform = type('GeoTransform', (tag, Node, ParentNode), {'name': 'GeoTransform', '__init__': x3dom_init})
geoViewpoint = GeoViewpoint = type('GeoViewpoint', (tag, Node, ParentNode), {'name': 'GeoViewpoint', '__init__': x3dom_init})
group = Group = type('Group', (tag, Node, ParentNode), {'name': 'Group', '__init__': x3dom_init})
hAnimDisplacer = HAnimDisplacer = type('HAnimDisplacer', (tag, Node, ParentNode), {'name': 'HAnimDisplacer', '__init__': x3dom_init})
hAnimHumanoid = HAnimHumanoid = type('HAnimHumanoid', (tag, Node, ParentNode), {'name': 'HAnimHumanoid', '__init__': x3dom_init})
hAnimJoint = HAnimJoint = type('HAnimJoint', (tag, Node, ParentNode), {'name': 'HAnimJoint', '__init__': x3dom_init})
hAnimSegment = HAnimSegment = type('HAnimSegment', (tag, Node, ParentNode), {'name': 'HAnimSegment', '__init__': x3dom_init})
hAnimSite = HAnimSite = type('HAnimSite', (tag, Node, ParentNode), {'name': 'HAnimSite', '__init__': x3dom_init})
imageTexture = ImageTexture = type('ImageTexture', (tag, Node, ParentNode), {'name': 'ImageTexture', '__init__': x3dom_init})
imageTexture3D = ImageTexture3D = type('ImageTexture3D', (tag, Node, ParentNode), {'name': 'ImageTexture3D', '__init__': x3dom_init})
imageTextureAtlas = ImageTextureAtlas = type('ImageTextureAtlas', (tag, Node, ParentNode), {'name': 'ImageTextureAtlas', '__init__': x3dom_init})
indexedFaceSet = IndexedFaceSet = type('IndexedFaceSet', (tag, Node, ParentNode), {'name': 'IndexedFaceSet', '__init__': x3dom_init})
indexedLineSet = IndexedLineSet = type('IndexedLineSet', (tag, Node, ParentNode), {'name': 'IndexedLineSet', '__init__': x3dom_init})
indexedQuadSet = IndexedQuadSet = type('IndexedQuadSet', (tag, Node, ParentNode), {'name': 'IndexedQuadSet', '__init__': x3dom_init})
indexedTriangleSet = IndexedTriangleSet = type('IndexedTriangleSet', (tag, Node, ParentNode), {'name': 'IndexedTriangleSet', '__init__': x3dom_init})
indexedTriangleStripSet = IndexedTriangleStripSet = type('IndexedTriangleStripSet', (tag, Node, ParentNode), {'name': 'IndexedTriangleStripSet', '__init__': x3dom_init})
isoSurfaceVolumeData = IsoSurfaceVolumeData = type('IsoSurfaceVolumeData', (tag, Node, ParentNode), {'name': 'IsoSurfaceVolumeData', '__init__': x3dom_init})
lineProperties = LineProperties = type('LineProperties', (tag, Node, ParentNode), {'name': 'LineProperties', '__init__': x3dom_init})
lineSet = LineSet = type('LineSet', (tag, Node, ParentNode), {'name': 'LineSet', '__init__': x3dom_init})
lOD = LOD = type('LOD', (tag, Node, ParentNode), {'name': 'LOD', '__init__': x3dom_init})
matrixTextureTransform = MatrixTextureTransform = type('MatrixTextureTransform', (tag, Node, ParentNode), {'name': 'MatrixTextureTransform', '__init__': x3dom_init})
matrixTransform = MatrixTransform = type('MatrixTransform', (tag, Node, ParentNode), {'name': 'MatrixTransform', '__init__': x3dom_init})
mesh = Mesh = type('Mesh', (tag, Node, ParentNode), {'name': 'Mesh', '__init__': x3dom_init})
metadataBoolean = MetadataBoolean = type('MetadataBoolean', (tag, Node, ParentNode), {'name': 'MetadataBoolean', '__init__': x3dom_init})
metadataDouble = MetadataDouble = type('MetadataDouble', (tag, Node, ParentNode), {'name': 'MetadataDouble', '__init__': x3dom_init})
metadataFloat = MetadataFloat = type('MetadataFloat', (tag, Node, ParentNode), {'name': 'MetadataFloat', '__init__': x3dom_init})
metadataInteger = MetadataInteger = type('MetadataInteger', (tag, Node, ParentNode), {'name': 'MetadataInteger', '__init__': x3dom_init})
metadataSet = MetadataSet = type('MetadataSet', (tag, Node, ParentNode), {'name': 'MetadataSet', '__init__': x3dom_init})
metadataString = MetadataString = type('MetadataString', (tag, Node, ParentNode), {'name': 'MetadataString', '__init__': x3dom_init})
motorJoint = MotorJoint = type('MotorJoint', (tag, Node, ParentNode), {'name': 'MotorJoint', '__init__': x3dom_init})
movieTexture = MovieTexture = type('MovieTexture', (tag, Node, ParentNode), {'name': 'MovieTexture', '__init__': x3dom_init})
mPRPlane = MPRPlane = type('MPRPlane', (tag, Node, ParentNode), {'name': 'MPRPlane', '__init__': x3dom_init})
mPRVolumeStyle = MPRVolumeStyle = type('MPRVolumeStyle', (tag, Node, ParentNode), {'name': 'MPRVolumeStyle', '__init__': x3dom_init})
multiTexture = MultiTexture = type('MultiTexture', (tag, Node, ParentNode), {'name': 'MultiTexture', '__init__': x3dom_init})
multiTextureCoordinate = MultiTextureCoordinate = type('MultiTextureCoordinate', (tag, Node, ParentNode), {'name': 'MultiTextureCoordinate', '__init__': x3dom_init})
navigationInfo = NavigationInfo = type('NavigationInfo', (tag, Node, ParentNode), {'name': 'NavigationInfo', '__init__': x3dom_init})
normal = Normal = type('Normal', (tag, Node, ParentNode), {'name': 'Normal', '__init__': x3dom_init})
normalInterpolator = NormalInterpolator = type('NormalInterpolator', (tag, Node, ParentNode), {'name': 'NormalInterpolator', '__init__': x3dom_init})
nozzle = Nozzle = type('Nozzle', (tag, Node, ParentNode), {'name': 'Nozzle', '__init__': x3dom_init})
opacityMapVolumeStyle = OpacityMapVolumeStyle = type('OpacityMapVolumeStyle', (tag, Node, ParentNode), {'name': 'OpacityMapVolumeStyle', '__init__': x3dom_init})
orientationChaser = OrientationChaser = type('OrientationChaser', (tag, Node, ParentNode), {'name': 'OrientationChaser', '__init__': x3dom_init})
orientationDamper = OrientationDamper = type('OrientationDamper', (tag, Node, ParentNode), {'name': 'OrientationDamper', '__init__': x3dom_init})
orientationInterpolator = OrientationInterpolator = type('OrientationInterpolator', (tag, Node, ParentNode), {'name': 'OrientationInterpolator', '__init__': x3dom_init})
orthoViewpoint = OrthoViewpoint = type('OrthoViewpoint', (tag, Node, ParentNode), {'name': 'OrthoViewpoint', '__init__': x3dom_init})
param = Param = type('Param', (tag, Node, ParentNode), {'name': 'Param', '__init__': x3dom_init})
particleSet = ParticleSet = type('ParticleSet', (tag, Node, ParentNode), {'name': 'ParticleSet', '__init__': x3dom_init})
physicalEnvironmentLight = PhysicalEnvironmentLight = type('PhysicalEnvironmentLight', (tag, Node, ParentNode), {'name': 'PhysicalEnvironmentLight', '__init__': x3dom_init})
physicalMaterial = PhysicalMaterial = type('PhysicalMaterial', (tag, Node, ParentNode), {'name': 'PhysicalMaterial', '__init__': x3dom_init})
pixelTexture = PixelTexture = type('PixelTexture', (tag, Node, ParentNode), {'name': 'PixelTexture', '__init__': x3dom_init})
pixelTexture3D = PixelTexture3D = type('PixelTexture3D', (tag, Node, ParentNode), {'name': 'PixelTexture3D', '__init__': x3dom_init})
planeSensor = PlaneSensor = type('PlaneSensor', (tag, Node, ParentNode), {'name': 'PlaneSensor', '__init__': x3dom_init})
pointLight = PointLight = type('PointLight', (tag, Node, ParentNode), {'name': 'PointLight', '__init__': x3dom_init})
pointSet = PointSet = type('PointSet', (tag, Node, ParentNode), {'name': 'PointSet', '__init__': x3dom_init})
polyline2D = Polyline2D = type('Polyline2D', (tag, Node, ParentNode), {'name': 'Polyline2D', '__init__': x3dom_init})
polypoint2D = Polypoint2D = type('Polypoint2D', (tag, Node, ParentNode), {'name': 'Polypoint2D', '__init__': x3dom_init})
popGeometry = PopGeometry = type('PopGeometry', (tag, Node, ParentNode), {'name': 'PopGeometry', '__init__': x3dom_init})
popGeometryLevel = PopGeometryLevel = type('PopGeometryLevel', (tag, Node, ParentNode), {'name': 'PopGeometryLevel', '__init__': x3dom_init})
positionChaser = PositionChaser = type('PositionChaser', (tag, Node, ParentNode), {'name': 'PositionChaser', '__init__': x3dom_init})
positionChaser2D = PositionChaser2D = type('PositionChaser2D', (tag, Node, ParentNode), {'name': 'PositionChaser2D', '__init__': x3dom_init})
positionDamper = PositionDamper = type('PositionDamper', (tag, Node, ParentNode), {'name': 'PositionDamper', '__init__': x3dom_init})
positionDamper2D = PositionDamper2D = type('PositionDamper2D', (tag, Node, ParentNode), {'name': 'PositionDamper2D', '__init__': x3dom_init})
positionInterpolator = PositionInterpolator = type('PositionInterpolator', (tag, Node, ParentNode), {'name': 'PositionInterpolator', '__init__': x3dom_init})
positionInterpolator2D = PositionInterpolator2D = type('PositionInterpolator2D', (tag, Node, ParentNode), {'name': 'PositionInterpolator2D', '__init__': x3dom_init})
projectionVolumeStyle = ProjectionVolumeStyle = type('ProjectionVolumeStyle', (tag, Node, ParentNode), {'name': 'ProjectionVolumeStyle', '__init__': x3dom_init})
pyramid = Pyramid = type('Pyramid', (tag, Node, ParentNode), {'name': 'Pyramid', '__init__': x3dom_init})
quadSet = QuadSet = type('QuadSet', (tag, Node, ParentNode), {'name': 'QuadSet', '__init__': x3dom_init})
radarVolumeStyle = RadarVolumeStyle = type('RadarVolumeStyle', (tag, Node, ParentNode), {'name': 'RadarVolumeStyle', '__init__': x3dom_init})
rectangle2D = Rectangle2D = type('Rectangle2D', (tag, Node, ParentNode), {'name': 'Rectangle2D', '__init__': x3dom_init})
rectangularTorus = RectangularTorus = type('RectangularTorus', (tag, Node, ParentNode), {'name': 'RectangularTorus', '__init__': x3dom_init})
refinementTexture = RefinementTexture = type('RefinementTexture', (tag, Node, ParentNode), {'name': 'RefinementTexture', '__init__': x3dom_init})
remoteSelectionGroup = RemoteSelectionGroup = type('RemoteSelectionGroup', (tag, Node, ParentNode), {'name': 'RemoteSelectionGroup', '__init__': x3dom_init})
renderedTexture = RenderedTexture = type('RenderedTexture', (tag, Node, ParentNode), {'name': 'RenderedTexture', '__init__': x3dom_init})
rigidBody = RigidBody = type('RigidBody', (tag, Node, ParentNode), {'name': 'RigidBody', '__init__': x3dom_init})
rigidBodyCollection = RigidBodyCollection = type('RigidBodyCollection', (tag, Node, ParentNode), {'name': 'RigidBodyCollection', '__init__': x3dom_init})
scalarChaser = ScalarChaser = type('ScalarChaser', (tag, Node, ParentNode), {'name': 'ScalarChaser', '__init__': x3dom_init})
scalarDamper = ScalarDamper = type('ScalarDamper', (tag, Node, ParentNode), {'name': 'ScalarDamper', '__init__': x3dom_init})
scalarInterpolator = ScalarInterpolator = type('ScalarInterpolator', (tag, Node, ParentNode), {'name': 'ScalarInterpolator', '__init__': x3dom_init})
segmentedVolumeData = SegmentedVolumeData = type('SegmentedVolumeData', (tag, Node, ParentNode), {'name': 'SegmentedVolumeData', '__init__': x3dom_init})
shadedVolumeStyle = ShadedVolumeStyle = type('ShadedVolumeStyle', (tag, Node, ParentNode), {'name': 'ShadedVolumeStyle', '__init__': x3dom_init})
shaderPart = ShaderPart = type('ShaderPart', (tag, Node, ParentNode), {'name': 'ShaderPart', '__init__': x3dom_init})
silhouetteEnhancementVolumeStyle = SilhouetteEnhancementVolumeStyle = type('SilhouetteEnhancementVolumeStyle', (tag, Node, ParentNode), {'name': 'SilhouetteEnhancementVolumeStyle', '__init__': x3dom_init})
singleAxisHingeJoint = SingleAxisHingeJoint = type('SingleAxisHingeJoint', (tag, Node, ParentNode), {'name': 'SingleAxisHingeJoint', '__init__': x3dom_init})
sliderJoint = SliderJoint = type('SliderJoint', (tag, Node, ParentNode), {'name': 'SliderJoint', '__init__': x3dom_init})
slopedCylinder = SlopedCylinder = type('SlopedCylinder', (tag, Node, ParentNode), {'name': 'SlopedCylinder', '__init__': x3dom_init})
snout = Snout = type('Snout', (tag, Node, ParentNode), {'name': 'Snout', '__init__': x3dom_init})
solidOfRevolution = SolidOfRevolution = type('SolidOfRevolution', (tag, Node, ParentNode), {'name': 'SolidOfRevolution', '__init__': x3dom_init})
sound = Sound = type('Sound', (tag, Node, ParentNode), {'name': 'Sound', '__init__': x3dom_init})
sphereSegment = SphereSegment = type('SphereSegment', (tag, Node, ParentNode), {'name': 'SphereSegment', '__init__': x3dom_init})
sphereSensor = SphereSensor = type('SphereSensor', (tag, Node, ParentNode), {'name': 'SphereSensor', '__init__': x3dom_init})
splinePositionInterpolator = SplinePositionInterpolator = type('SplinePositionInterpolator', (tag, Node, ParentNode), {'name': 'SplinePositionInterpolator', '__init__': x3dom_init})
spotLight = SpotLight = type('SpotLight', (tag, Node, ParentNode), {'name': 'SpotLight', '__init__': x3dom_init})
staticGroup = StaticGroup = type('StaticGroup', (tag, Node, ParentNode), {'name': 'StaticGroup', '__init__': x3dom_init})
stippleVolumeStyle = StippleVolumeStyle = type('StippleVolumeStyle', (tag, Node, ParentNode), {'name': 'StippleVolumeStyle', '__init__': x3dom_init})
surfaceShaderTexture = SurfaceShaderTexture = type('SurfaceShaderTexture', (tag, Node, ParentNode), {'name': 'SurfaceShaderTexture', '__init__': x3dom_init})
switch = Switch = type('Switch', (tag, Node, ParentNode), {'name': 'Switch', '__init__': x3dom_init})
texCoordDamper2D = TexCoordDamper2D = type('TexCoordDamper2D', (tag, Node, ParentNode), {'name': 'TexCoordDamper2D', '__init__': x3dom_init})
text = Text = type('Text', (tag, Node, ParentNode), {'name': 'Text', '__init__': x3dom_init})
texture = Texture = type('Texture', (tag, Node, ParentNode), {'name': 'Texture', '__init__': x3dom_init})
textureCoordinate = TextureCoordinate = type('TextureCoordinate', (tag, Node, ParentNode), {'name': 'TextureCoordinate', '__init__': x3dom_init})
textureCoordinate3D = TextureCoordinate3D = type('TextureCoordinate3D', (tag, Node, ParentNode), {'name': 'TextureCoordinate3D', '__init__': x3dom_init})
textureCoordinateGenerator = TextureCoordinateGenerator = type('TextureCoordinateGenerator', (tag, Node, ParentNode), {'name': 'TextureCoordinateGenerator', '__init__': x3dom_init})
textureProperties = TextureProperties = type('TextureProperties', (tag, Node, ParentNode), {'name': 'TextureProperties', '__init__': x3dom_init})
textureTransform = TextureTransform = type('TextureTransform', (tag, Node, ParentNode), {'name': 'TextureTransform', '__init__': x3dom_init})
textureTransform3D = TextureTransform3D = type('TextureTransform3D', (tag, Node, ParentNode), {'name': 'TextureTransform3D', '__init__': x3dom_init})
textureTransformMatrix3D = TextureTransformMatrix3D = type('TextureTransformMatrix3D', (tag, Node, ParentNode), {'name': 'TextureTransformMatrix3D', '__init__': x3dom_init})
toneMappedVolumeStyle = ToneMappedVolumeStyle = type('ToneMappedVolumeStyle', (tag, Node, ParentNode), {'name': 'ToneMappedVolumeStyle', '__init__': x3dom_init})
torus = Torus = type('Torus', (tag, Node, ParentNode), {'name': 'Torus', '__init__': x3dom_init})
touchSensor = TouchSensor = type('TouchSensor', (tag, Node, ParentNode), {'name': 'TouchSensor', '__init__': x3dom_init})
triangleSet = TriangleSet = type('TriangleSet', (tag, Node, ParentNode), {'name': 'TriangleSet', '__init__': x3dom_init})
triangleSet2D = TriangleSet2D = type('TriangleSet2D', (tag, Node, ParentNode), {'name': 'TriangleSet2D', '__init__': x3dom_init})
twoSidedMaterial = TwoSidedMaterial = type('TwoSidedMaterial', (tag, Node, ParentNode), {'name': 'TwoSidedMaterial', '__init__': x3dom_init})
uniform = Uniform = type('Uniform', (tag, Node, ParentNode), {'name': 'Uniform', '__init__': x3dom_init})
universalJoint = UniversalJoint = type('UniversalJoint', (tag, Node, ParentNode), {'name': 'UniversalJoint', '__init__': x3dom_init})
viewfrustum = Viewfrustum = type('Viewfrustum', (tag, Node, ParentNode), {'name': 'Viewfrustum', '__init__': x3dom_init})
viewpoint = Viewpoint = type('Viewpoint', (tag, Node, ParentNode), {'name': 'Viewpoint', '__init__': x3dom_init})
volumeData = VolumeData = type('VolumeData', (tag, Node, ParentNode), {'name': 'VolumeData', '__init__': x3dom_init})
worldInfo = WorldInfo = type('WorldInfo', (tag, Node, ParentNode), {'name': 'WorldInfo', '__init__': x3dom_init})
x3DAppearanceChildNode = X3DAppearanceChildNode = type('X3DAppearanceChildNode', (tag, Node, ParentNode), {'name': 'X3DAppearanceChildNode', '__init__': x3dom_init})
x3DAppearanceNode = X3DAppearanceNode = type('X3DAppearanceNode', (tag, Node, ParentNode), {'name': 'X3DAppearanceNode', '__init__': x3dom_init})
x3DBackgroundNode = X3DBackgroundNode = type('X3DBackgroundNode', (tag, Node, ParentNode), {'name': 'X3DBackgroundNode', '__init__': x3dom_init})
x3DBinaryContainerGeometryNode = X3DBinaryContainerGeometryNode = type('X3DBinaryContainerGeometryNode', (tag, Node, ParentNode), {'name': 'X3DBinaryContainerGeometryNode', '__init__': x3dom_init})
x3DBindableNode = X3DBindableNode = type('X3DBindableNode', (tag, Node, ParentNode), {'name': 'X3DBindableNode', '__init__': x3dom_init})
x3DBoundedObject = X3DBoundedObject = type('X3DBoundedObject', (tag, Node, ParentNode), {'name': 'X3DBoundedObject', '__init__': x3dom_init})
x3DChaserNode = X3DChaserNode = type('X3DChaserNode', (tag, Node, ParentNode), {'name': 'X3DChaserNode', '__init__': x3dom_init})
x3DChildNode = X3DChildNode = type('X3DChildNode', (tag, Node, ParentNode), {'name': 'X3DChildNode', '__init__': x3dom_init})
x3DColorNode = X3DColorNode = type('X3DColorNode', (tag, Node, ParentNode), {'name': 'X3DColorNode', '__init__': x3dom_init})
x3DComposableVolumeRenderStyleNode = X3DComposableVolumeRenderStyleNode = type('X3DComposableVolumeRenderStyleNode', (tag, Node, ParentNode), {'name': 'X3DComposableVolumeRenderStyleNode', '__init__': x3dom_init})
x3DComposedGeometryNode = X3DComposedGeometryNode = type('X3DComposedGeometryNode', (tag, Node, ParentNode), {'name': 'X3DComposedGeometryNode', '__init__': x3dom_init})
x3DCoordinateNode = X3DCoordinateNode = type('X3DCoordinateNode', (tag, Node, ParentNode), {'name': 'X3DCoordinateNode', '__init__': x3dom_init})
x3DDamperNode = X3DDamperNode = type('X3DDamperNode', (tag, Node, ParentNode), {'name': 'X3DDamperNode', '__init__': x3dom_init})
x3DDragSensorNode = X3DDragSensorNode = type('X3DDragSensorNode', (tag, Node, ParentNode), {'name': 'X3DDragSensorNode', '__init__': x3dom_init})
x3DEnvironmentNode = X3DEnvironmentNode = type('X3DEnvironmentNode', (tag, Node, ParentNode), {'name': 'X3DEnvironmentNode', '__init__': x3dom_init})
x3DEnvironmentTextureNode = X3DEnvironmentTextureNode = type('X3DEnvironmentTextureNode', (tag, Node, ParentNode), {'name': 'X3DEnvironmentTextureNode', '__init__': x3dom_init})
x3DFogNode = X3DFogNode = type('X3DFogNode', (tag, Node, ParentNode), {'name': 'X3DFogNode', '__init__': x3dom_init})
x3DFollowerNode = X3DFollowerNode = type('X3DFollowerNode', (tag, Node, ParentNode), {'name': 'X3DFollowerNode', '__init__': x3dom_init})
x3DFontStyleNode = X3DFontStyleNode = type('X3DFontStyleNode', (tag, Node, ParentNode), {'name': 'X3DFontStyleNode', '__init__': x3dom_init})
x3DGeometricPropertyNode = X3DGeometricPropertyNode = type('X3DGeometricPropertyNode', (tag, Node, ParentNode), {'name': 'X3DGeometricPropertyNode', '__init__': x3dom_init})
x3DGeometryNode = X3DGeometryNode = type('X3DGeometryNode', (tag, Node, ParentNode), {'name': 'X3DGeometryNode', '__init__': x3dom_init})
x3DGroupingNode = X3DGroupingNode = type('X3DGroupingNode', (tag, Node, ParentNode), {'name': 'X3DGroupingNode', '__init__': x3dom_init})
x3DInfoNode = X3DInfoNode = type('X3DInfoNode', (tag, Node, ParentNode), {'name': 'X3DInfoNode', '__init__': x3dom_init})
x3DInterpolatorNode = X3DInterpolatorNode = type('X3DInterpolatorNode', (tag, Node, ParentNode), {'name': 'X3DInterpolatorNode', '__init__': x3dom_init})
x3DLightNode = X3DLightNode = type('X3DLightNode', (tag, Node, ParentNode), {'name': 'X3DLightNode', '__init__': x3dom_init})
x3DLODNode = X3DLODNode = type('X3DLODNode', (tag, Node, ParentNode), {'name': 'X3DLODNode', '__init__': x3dom_init})
x3DMaterialNode = X3DMaterialNode = type('X3DMaterialNode', (tag, Node, ParentNode), {'name': 'X3DMaterialNode', '__init__': x3dom_init})
x3DMetadataObject = X3DMetadataObject = type('X3DMetadataObject', (tag, Node, ParentNode), {'name': 'X3DMetadataObject', '__init__': x3dom_init})
x3DNavigationInfoNode = X3DNavigationInfoNode = type('X3DNavigationInfoNode', (tag, Node, ParentNode), {'name': 'X3DNavigationInfoNode', '__init__': x3dom_init})
x3DNBodyCollidableNode = X3DNBodyCollidableNode = type('X3DNBodyCollidableNode', (tag, Node, ParentNode), {'name': 'X3DNBodyCollidableNode', '__init__': x3dom_init})
x3DNode = X3DNode = type('X3DNode', (tag, Node, ParentNode), {'name': 'X3DNode', '__init__': x3dom_init})
x3DPlanarGeometryNode = X3DPlanarGeometryNode = type('X3DPlanarGeometryNode', (tag, Node, ParentNode), {'name': 'X3DPlanarGeometryNode', '__init__': x3dom_init})
x3DPointingDeviceSensorNode = X3DPointingDeviceSensorNode = type('X3DPointingDeviceSensorNode', (tag, Node, ParentNode), {'name': 'X3DPointingDeviceSensorNode', '__init__': x3dom_init})
x3DRigidJointNode = X3DRigidJointNode = type('X3DRigidJointNode', (tag, Node, ParentNode), {'name': 'X3DRigidJointNode', '__init__': x3dom_init})
x3DSensorNode = X3DSensorNode = type('X3DSensorNode', (tag, Node, ParentNode), {'name': 'X3DSensorNode', '__init__': x3dom_init})
x3DShaderNode = X3DShaderNode = type('X3DShaderNode', (tag, Node, ParentNode), {'name': 'X3DShaderNode', '__init__': x3dom_init})
x3DShapeNode = X3DShapeNode = type('X3DShapeNode', (tag, Node, ParentNode), {'name': 'X3DShapeNode', '__init__': x3dom_init})
x3DSoundNode = X3DSoundNode = type('X3DSoundNode', (tag, Node, ParentNode), {'name': 'X3DSoundNode', '__init__': x3dom_init})
x3DSoundSourceNode = X3DSoundSourceNode = type('X3DSoundSourceNode', (tag, Node, ParentNode), {'name': 'X3DSoundSourceNode', '__init__': x3dom_init})
x3DSpatialGeometryNode = X3DSpatialGeometryNode = type('X3DSpatialGeometryNode', (tag, Node, ParentNode), {'name': 'X3DSpatialGeometryNode', '__init__': x3dom_init})
x3DTexture3DNode = X3DTexture3DNode = type('X3DTexture3DNode', (tag, Node, ParentNode), {'name': 'X3DTexture3DNode', '__init__': x3dom_init})
x3DTextureCoordinateNode = X3DTextureCoordinateNode = type('X3DTextureCoordinateNode', (tag, Node, ParentNode), {'name': 'X3DTextureCoordinateNode', '__init__': x3dom_init})
x3DTextureNode = X3DTextureNode = type('X3DTextureNode', (tag, Node, ParentNode), {'name': 'X3DTextureNode', '__init__': x3dom_init})
x3DTextureTransformNode = X3DTextureTransformNode = type('X3DTextureTransformNode', (tag, Node, ParentNode), {'name': 'X3DTextureTransformNode', '__init__': x3dom_init})
x3DTimeDependentNode = X3DTimeDependentNode = type('X3DTimeDependentNode', (tag, Node, ParentNode), {'name': 'X3DTimeDependentNode', '__init__': x3dom_init})
x3DTouchSensorNode = X3DTouchSensorNode = type('X3DTouchSensorNode', (tag, Node, ParentNode), {'name': 'X3DTouchSensorNode', '__init__': x3dom_init})
x3DTransformNode = X3DTransformNode = type('X3DTransformNode', (tag, Node, ParentNode), {'name': 'X3DTransformNode', '__init__': x3dom_init})
x3DVertexAttributeNode = X3DVertexAttributeNode = type('X3DVertexAttributeNode', (tag, Node, ParentNode), {'name': 'X3DVertexAttributeNode', '__init__': x3dom_init})
x3DViewpointNode = X3DViewpointNode = type('X3DViewpointNode', (tag, Node, ParentNode), {'name': 'X3DViewpointNode', '__init__': x3dom_init})
x3DVolumeDataNode = X3DVolumeDataNode = type('X3DVolumeDataNode', (tag, Node, ParentNode), {'name': 'X3DVolumeDataNode', '__init__': x3dom_init})
x3DVolumeRenderStyleNode = X3DVolumeRenderStyleNode = type('X3DVolumeRenderStyleNode', (tag, Node, ParentNode), {'name': 'X3DVolumeRenderStyleNode', '__init__': x3dom_init})