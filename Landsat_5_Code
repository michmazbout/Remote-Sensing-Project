// Define the Aletsch Glacier polygon
var aletschGlacier = ee.Geometry.Polygon([
  [7.753666679263547, 45.97736091289284],
  [7.752465049624875, 45.977629325529776],
  [7.751520912051633, 45.97795738365248],
  [7.750705520511105, 45.97867314008293],
  [7.7489030760530975, 45.97980640217593],
  [7.746542732119992, 45.98144660886178],
  [7.744525710940793, 45.98284820152748],
  [7.742680351138547, 45.984190118702415],
  [7.738875878106137, 45.98388670881146],
  [7.738232147942563, 45.982992096072635],
  [7.737288010369321, 45.981858899183855],
  [7.737288010369321, 45.98021870471198],
  [7.738532555352231, 45.978995982676096],
  [7.740506661187192, 45.97675922615227],
  [7.740678322564145, 45.97535747934542],
  [7.741107476006528, 45.974522379275406],
  [7.741922867547055, 45.97425395157846],
  [7.744040711777163, 45.97321351329478],
  [7.7443411191868305, 45.9716923698588],
  [7.755499108688784, 45.97750828100394],
  [7.753666679263547, 45.97736091289284]
]);
// get the images from the landsat 5
// it only loads the part close to the polygon
// Then we filter the sattelite images with 15% cloud cover or less
var dataset = ee.ImageCollection('LANDSAT/LT05/C02/T1_L2')
    .filterBounds(aletschGlacier)
    .filterDate('1985-01-01', '2010-12-30')
    .filter(ee.Filter.lt('CLOUD_COVER', 15));
    
// Applies scaling factors.
function applyScaleFactors(image) {
  var opticalBands = image.select('SR_B.').multiply(0.0000275).add(-0.2);
  var thermalBand = image.select('ST_B6').multiply(0.00341802).add(149.0);
  return image.addBands(opticalBands, null, true)
              .addBands(thermalBand, null, true);
}
// applies the scale set before to everything
dataset = dataset.map(applyScaleFactors);
// changes the name of the bands to SR_Bx instead of Bx
var visualization = {
  bands: ['SR_B3', 'SR_B2', 'SR_B1'],
  min: 0.0,
  max: 0.3,
};
// centers the map around this point
Map.setCenter(-114.2579, 38.9275, 8);
// adds color to everything for visualization
Map.addLayer(dataset, visualization, 'True Color (321)');

// Add the Aletsch Glacier polygon to the map
Map.centerObject(aletschGlacier, 9);
// colors the layer blue
Map.addLayer(aletschGlacier, {color: 'blue'}, 'Aletsch Glacier');
// picks the first image from all the images we got
var image = dataset.first();
// Puts the image info in the console
print(image)

// Calculate Normalized Difference Snow Index (NDSI)
var ndsi = image.normalizedDifference(['SR_B2', 'SR_B5']);

// Create a binary snow cover mask based on NDSI threshold
var snow_mask = ndsi.gt(0.4);

snow_mask = snow_mask.focal_mode();

// Display the result
Map.addLayer(snow_mask, {palette: '000000, ff0000', opacity: 0.45}, 'Snow Cover');

// Function to calculate ice area for a given image
function calculateIceArea(image) {
  var ndsi = image.normalizedDifference(['SR_B2', 'SR_B5']);
  var snow_mask = ndsi.gt(0.4);
  var iceMaskFiltered = snow_mask.focal_mode();
  var area = iceMaskFiltered.reduceRegion({
    reducer: ee.Reducer.sum(),
    geometry: aletschGlacier,
    scale: 30, // Adjust the scale based on your needs
  });
  return ee.Feature(null, { area: area.get('nd') });
}

// Map over all images meaning it goes through all the images and runs the function on it
var iceAreaCollection = dataset.map(calculateIceArea);

// Print the result
print(iceAreaCollection);

/////////////////////////////////////////////////////
// Exploration
/////////////////////////////////////////////////////
// Get the QA band (SR_CLOUD_QA)
//var qa_band = image.select(['QA_PIXEL']);

// Define the snow bit (Bit 4)
//var snow_bit = 1 << 5;
//var water_bit = 1 << 7;

// Create a snow mask
//var snow_mask = qa_band.bitwiseAnd(snow_bit).neq(0);
//var water_mask = qa_band.bitwiseAnd(water_bit).neq(0);

// Display the result
//Map.addLayer(snow_mask, {palette: '000000, ff0000', opacity: 0.45}, 'Snow Cover');
//Map.addLayer(water_mask, {palette: '000000, 00aeff', opacity: 0.45}, 'Water Cover');

/////////////////////////////////////////////////////
//Exploration For Date and pixel size
/////////////////////////////////////////////////////

// Your FeatureCollection
var yourFeatureCollection = iceAreaCollection /* your FeatureCollection here */;

// Function to extract date and area from each feature
var extractProperties = function(feature) {
  var date = ee.String(feature.id().get('date'));
  var area = ee.Number(feature.get('area'));

  // Create a new feature with date and area properties
  return ee.Feature(null, {
    'date': date,
    'area': area
  });
};

// Map over the FeatureCollection and apply the function
//var extractedFeatures = yourFeatureCollection.map(extractProperties);

// Print the new FeatureCollection
//print(extractedFeatures);

// Function to extract date and area from each feature
var extractProperties = function(feature) {
  // Extract date from feature ID
  var dateString = ee.String(feature.id()).slice(12, 20);
  var date = dateString//ee.Date.parse('YYYYMMDD', dateString);

  // Get area from properties
  var area = ee.Number(feature.get('area'));

  // Create a new feature with date and area properties
  return ee.Feature(null, {
    'date': date,
    'area': area
  });
};

// Map over the FeatureCollection and apply the function
var extractedFeatures = yourFeatureCollection.map(extractProperties);
print(extractedFeatures)

Export.table.toDrive({
  collection: extractedFeatures,
  description:'vectorsToDriveExample',
  fileFormat: 'CSV'
});
