var request = require("request");
const mraa = require('mraa');

var analogPin_0 = new mraa.Aio(0);

var idCount = 0;
var sensorJsonData = {
  "id": 0,
  "name": "",
  "value": 0,
};

function getValue(){
    var analogValue_Temp = analogPin_0.readFloat();
    return analogValue_Temp.toFixed(2);
}

function datSendFromSensor(){
  sensorJsonData.id = idCount++;
  sensorJsonData.name = "Temp";
  sensorJsonData.value = getValue();
  request({
      method: "POST",
      url: "http://192.168.4.242:5000/postdata",
      headers: {
          "content-type" : "application/json",
      },
      json:true,
      body: sensorJsonData
  },function(err, res, body){});
  console.log(sensorJsonData.id);
  console.log(sensorJsonData.name);
  console.log(sensorJsonData.value);
}

setInterval(function(){
    datSendFromSensor();
},5000);



