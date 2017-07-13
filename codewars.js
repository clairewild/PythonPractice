function tickets(peopleInLine){
  twenty_fives = 0;
  fifties = 0;
  transactions = 0;
  peopleInLine.forEach(function(x) {
    if (x == 25) {twenty_fives += 1;}
    else if (x == 50) {fifties += 1;}
    change = x - 25;
    for (t = 0; t <= twenty_fives; t++) {
      for (f = 0; f <= fifties; f++) {
        if (f * 50 + t * 25 == change) {
          transactions += 1;
          twenty_fives -= t;
          fifties -= f;
          return;
        }
      }
    }
  });
  if (transactions == peopleInLine.length) {
    return "YES";
  }
  else {return "NO";}

// Takes a string and returns true if all parenthesis are paired correctly
function groupCheck(s) {
  str = s.replace(/\s|\w/gi, "");
  if (str == "") {
     return true;
  }
  if (str.length == 2) {
    if (matchBrackets(str.charAt(0), str.charAt(1))) {
      return true;
    }
    else {
      return false;
    }
  }
  else {
    for (i = 0; i < str.length; i++) {
      if (["\(", "\[", "\{"].indexOf(str.charAt(i)) > -1 && ["\)", "\]", "\}"].indexOf(str.charAt(i + 1)) > -1) {
        if (matchBrackets(str.charAt(i), str.charAt(i + 1))) {
          newString = str.substring(0, i) + str.substring(i + 2, str.length);
          return groupCheck(newString);
        }
        else {
          return false;
        }
      }
    }
  }
}

// Checks to see if two strings are a pair of parenthesis
function matchBrackets(one, two) {
  if (one == "\(" && two == "\)") {
    return true;
  }
  else if (one == "\[" && two == "\]") {
    return true;
  }
  else if (one == "\{" && two == "\}") {
    return true;
  }
  else {
    return false;
  }
}

// Parenthesis version 2
function validBraces(braces) {
   if (braces.length == 0) {
     return true;
   }
   if (braces.length == 1) {
     return false;
   }
   if (braces.length % 2 != 0) {
     return false;
   }
   newString = braces.replace(/\(\)|\[\]|\{\}/g, "");
   if (newString.length == braces.length) {
     return false;
   }
   else {
     return validBraces(newString);
   }
}

// Takes an int and adds the digits, then adds the digits of the sum, until find one digit root
function digital_root(n) {
  if (n < 10) {
    return n;
  }
  else {
    digits = n.toString().split("").map(function(x) {return parseInt(x)});
    sum = 0;
    for (i = 0; i < digits.length; i++) {
      sum += digits[i];
    }
    return digital_root(sum);
  }
}

// Using a dictionary MORSE_CODE, takes a string of morse words separated by 3 spaces and returns a readable string
decodeMorse = function(morseCode) {
  morseWords = morseCode.trim().split("   ");
  message = [];
  for (j = 0; j < morseWords.length; j++) {
    word = morseWords[j].split(" ");
    for (i = 0; i < word.length; i++) {
      message.push(MORSE_CODE[word[i]]);
    }
    message.push(" ");
  }
  return message.join("").trim();
}

// Takes an array of integers, and returns an object with arrays of the indexes and values of local peaks
function pickPeaks(arr){
  result = {pos: [], peaks: []};
  if (arr.length > 2) {
    arr.forEach(function(x, i){
      if (i < arr.length - 2) {
        j = i + 1;
        k = i + 2;
        while (k < arr.length) {
          if (arr[j] == arr[k]) {
            k++;
          }
          else {
            break;
          }
        }
        if ((arr[i] < arr[j]) && (arr[j] > arr[k])) {
           result.pos.push(j);
           result.peaks.push(arr[j]);
        }
      }
    });
  }
  return result;
}

// Takes a string, and returns an encoded string where every letter is shifted along 13 letter in alphabet
function rot13(message){
  encoded = [];
  for (i = 0; i < message.length; i++) {
    letter = message.charAt(i);
    code = message.charCodeAt(i);
    if (letter.match(/[a-m]|[A-M]/g) != null) {
      encoded.push(String.fromCharCode(code + 13));
    }
    else if (letter.match(/[n-z]|[N-Z]/g) != null) {
      encoded.push(String.fromCharCode(code - 13));
    }
    else {
      encoded.push(letter);
    }
  }
  return encoded.join("");
}
