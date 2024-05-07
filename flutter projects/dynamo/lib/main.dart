import 'package:flutter/material.dart';

void main(){
  runApp(const MApp());
}
class MApp extends StatefulWidget{
 const MApp({ super.key }); 
 @override
 State createState() => Stateful();

}
class Stateful extends State{
   @override
  Widget build(BuildContext context){
    double currency = 0;
    TextEditingController inputCurrency = TextEditingController();
    return MaterialApp(
      home: Scaffold(
        backgroundColor: const Color.fromARGB(255, 6, 139, 142),
        body:Column(
          
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
           const Text("Convert your currency",
             style: TextStyle(
              color: Color.fromARGB(255, 253, 253, 253),
              fontSize: 25,
              fontWeight: FontWeight.bold,
             ),
            ),
             Padding(
              padding: const EdgeInsets.all(16.0),
              child: TextField(
                controller: inputCurrency,
                keyboardType: TextInputType.number,
                decoration: InputDecoration(
                  prefixIcon: Icon(Icons.monetization_on),
                  fillColor: Colors.white,
                  filled: true,
                  hintText: "Enter you currency in USD",
                  hintStyle: TextStyle(
                    color: Colors.black,
                  fontSize: 18,
                  fontWeight: FontWeight.w200,
                  ),
                ),
                style: TextStyle(
                  color: Colors.black,
                  fontSize: 18,
                  ),
              ),
            ),
            ElevatedButton(
             style: const ButtonStyle(
                //  backgroundColor: MaterialStatePropertyAll(Colors.black),
                //  textStyle: MaterialStatePropertyAll(Color: Colors.white),
              ),
             onPressed: (){
              setState(() {
                currency = (double.parse(inputCurrency.text))*81;
              });
             },
             child: const Text("Convert"),

             ),
              Text(currency.toString(),
             style: TextStyle(
              color: Color.fromARGB(255, 253, 253, 253),
              fontSize: 25,
              fontWeight: FontWeight.bold,
             ),
            ),

          ],
        ),
      ),
    );
  }
}




// class MyApp extends StatelessWidget{
//   const MyApp({ super.key });
//   @override
//   Widget build(BuildContext context){
//     double currency = 0;
//     TextEditingController inputCurrency = TextEditingController();
//     return  MaterialApp(
//       home: Scaffold(
//         backgroundColor: const Color.fromARGB(255, 6, 139, 142),
//         body:Column(
          
//           mainAxisAlignment: MainAxisAlignment.center,
//           children: [
//            const Text("Convert your currency",
//              style: TextStyle(
//               color: Color.fromARGB(255, 253, 253, 253),
//               fontSize: 25,
//               fontWeight: FontWeight.bold,
//              ),
//             ),
//              Padding(
//               padding: const EdgeInsets.all(16.0),
//               child: TextField(
//                 controller: inputCurrency,
//                 keyboardType: TextInputType.number,
//                 decoration: InputDecoration(
//                   prefixIcon: Icon(Icons.monetization_on),
//                   fillColor: Colors.white,
//                   filled: true,
//                   hintText: "Enter you currency in USD",
//                   hintStyle: TextStyle(
//                     color: Colors.black,
//                   fontSize: 18,
//                   fontWeight: FontWeight.w200,
//                   ),
//                 ),
//                 style: TextStyle(
//                   color: Colors.black,
//                   fontSize: 18,
//                   ),
//               ),
//             ),
//             ElevatedButton(
//              style: const ButtonStyle(
//                 //  backgroundColor: MaterialStatePropertyAll(Colors.black),
//                 //  textStyle: MaterialStatePropertyAll(Color: Colors.white),
//               ),
//              onPressed: (){
              
//              },
//              child: const Text("Convert"),

//              ),
//               Text(currency.toString(),
//              style: TextStyle(
//               color: Color.fromARGB(255, 253, 253, 253),
//               fontSize: 25,
//               fontWeight: FontWeight.bold,
//              ),
//             ),

//           ],
//         ),
//       ),
//     );
//   }
// }
