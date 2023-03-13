function generateOTP(digits) {
    let numbers = '0123456789';
    let otp = '';
    for (var i=0;i<digits;i++){
        otp += numbers[Math.floor(Math.random()*10)];
    }
    return otp;
}

console.log(generateOTP(6));
console.log(generateOTP(4));
