// Define function which goes into prediction 
var deafault_dict = { 
   options: [
      {"Inflight Entertaiment": 3, 
      "Seat comfort": 3, 
      "Ease of Online booking": 3},
      {"Inflight Entertaiment": 4, 
      "Seat comfort": 3, 
      "Ease of Online booking": 3},
      {"Inflight Entertaiment": 5, 
      "Seat comfort": 3, 
      "Ease of Online booking": 3},
      {"Inflight Entertaiment": 3, 
      "Seat comfort": 4, 
      "Ease of Online booking": 3},
      {"Inflight Entertaiment": 3, 
      "Seat comfort": 5, 
      "Ease of Online booking": 3},
      {"Inflight Entertaiment": 3, 
      "Seat comfort": 3, 
      "Ease of Online booking": 4},
      {"Inflight Entertaiment": 3, 
      "Seat comfort": 3, 
      "Ease of Online booking": 5}],
   results: [
      [["Satisfied", 45.0],
      ["NotSatisfied", 55.0]],
      [["Satisfied", 47.0],
      ["NotSatisfied", 53.0]],
      [["Satisfied", 49.0],
      ["NotSatisfied", 51.0]],
      [["Satisfied", 41.0,]
      ["NotSatisfied", 59.0]],
      [["Satisfied", 40.0],
      ["NotSatisfied", 60.0]],
      [["Satisfied", 39.0],
      ["NotSatisfied", 61.0]],
      [["Satisfied", 44.0],
      ["NotSatisfied", 56.0]]
]}


var newdata = deafault_dict["results"][0]

var current_selection = {
   "Inflight Entertaiment": 3, 
   "Seat comfort": 3, 
   "Ease of Online booking": 4}

console.log(current_selection)

function EaseofOnlinebookingChanged(value) {
   // console.log(value)
   current_selection["Ease of Online booking"] = parseInt(value);
   console.log(current_selection)

   // find matching

   var test = deafault_dict["options"].findIndex(check)

   function check(item) {
      return JSON.stringify(current_selection) === JSON.stringify(item);
    }

   console.log(test)

   newdata = deafault_dict["results"][test]
 

   // deafault_dict["options"].forEach(function(item) { //loop through keys array

   //    ages.findIndex(checkAge)

   //    if (JSON.stringify(current_selection) === JSON.stringify(item)){
   //       console.log('yes')
   //       var keys = Object.keys(item)
   //       console.log(keys)
   //    }
   //    else 
   //    {
   //       console.log('no')
   //    }

   // });
   Highcharts.setOptions({
      plotOptions: {
         series: {
            animation: false
         }
      },
   });
   
   $(document).ready(function() {
      var chart = {
         plotBackgroundColor: null,
         plotBorderWidth: null,
         plotShadow: false,
         plotAreaWidth: 550,
         plotAreaHeight: 400,
         height: 400,
         width: 550,
         margin: [50,50,50,50]
      };
      var title = {
         text: 'Customers satifsaction (%)'   
      };      
      var tooltip = {
         pointFormat: '<b>{point.percentage:.1f}%</b>'
      };
      var plotOptions = {
         pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            
            dataLabels: {
               enabled: false,
               format: '<b>{point.name}</b>: {point.percentage:.1f} %',
               style: {
                  color: (Highcharts.theme && Highcharts.theme.contrastTextColor)||
                  'black'
               }
            }
         }
      };
      var series = [{
         type: 'pie',
         innerSize: '50%',
         name: 'Customers ',
         data: [
            newdata[0],
            newdata[1]
            //   {
            //      name: 'Chrome',
            //      y: 12.8,
            //      sliced: true,
            //      selected: true
            //   },
            //   ['Safari',    8.5],
            //   ['Opera',     6.2],
            //   ['Others',   0.7]
         ]
      }];
      // Radialize the colors
      if (!Highcharts.charts.length) {
         Highcharts.getOptions().colors = Highcharts.map(
            Highcharts.getOptions().colors, function (color) {
               return {
                  radialGradient: { cx: 0.5, cy: 0.3, r: 0.7 },
                  stops: [
                     [0, color],
                     [1, Highcharts.Color(color).brighten(-0.3).get('rgb')] // darken
                  ]
               };
            }
         );
      }
      
      var json = {};   
      json.chart = chart; 
      json.title = title;     
      json.tooltip = tooltip;  
      json.series = series;
      json.plotOptions = plotOptions;
      $('#container').highcharts(json);  
      });


}

Highcharts.setOptions({

   colors: ['#007bff', '#dc3545']
});

$(document).ready(function() {
   var chart = {
      plotBackgroundColor: null,
      plotBorderWidth: null,
      plotShadow: false,
      plotAreaWidth: 300,
      plotAreaHeight: 300,
      margin: [30,30,70,30]
   };
   var title = {
      text: 'Customers satifsaction (%)'   
   };      
   var tooltip = {
      pointFormat: '<b>{point.percentage:.1f}%</b>'
   };
   var plotOptions = {
      pie: {
         allowPointSelect: true,
         cursor: 'pointer',
         
         dataLabels: {
            enabled: true,
            format: '<b>{point.name}</b>: {point.percentage:.1f} %',
            style: {
               color: (Highcharts.theme && Highcharts.theme.contrastTextColor)||
               'black'
            }
         }
      }
   };
   var series = [{
      type: 'pie',
      innerSize: '50%',
      name: 'Customers ',
      data: [
         newdata[0],
         newdata[1]
         //   {
         //      name: 'Chrome',
         //      y: 12.8,
         //      sliced: true,
         //      selected: true
         //   },
         //   ['Safari',    8.5],
         //   ['Opera',     6.2],
         //   ['Others',   0.7]
      ]
   }];
   // Radialize the colors
   Highcharts.getOptions().colors = Highcharts.map(
      Highcharts.getOptions().colors, function (color) {
         return {
            radialGradient: { cx: 0.5, cy: 0.3, r: 0.7 },
            stops: [
               [0, color],
               [1, Highcharts.Color(color).brighten(-0.3).get('rgb')] // darken
            ]
         };
      }
   );
   
   var json = {};   
   json.chart = chart; 
   json.title = title;     
   json.tooltip = tooltip;  
   json.series = series;
   json.plotOptions = plotOptions;
   $('#container').highcharts(json);  
   });
