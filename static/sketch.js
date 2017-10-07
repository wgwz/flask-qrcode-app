var capture;

function setup() {
  createCanvas(1280, 960);
  capture = createCapture(VIDEO);
  capture.size(1280, 960);
}

function draw() {
  background(255);
  image(capture, 0, 0, 1280, 960);
}
