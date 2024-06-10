function calculateSeries(n) {
    if (n < 2) {
      throw new Error('Invalid input');
    }
  
    let cur = 0;
    for (let i = 2; i <= n; i++) {
      cur += 1 / (i * (i - 1));
    }
  
    return cur;
  }

  //The calculateSeries function calculates the series by iterating from 2 to n and accumulating the sum in the cur variable.
  // The loop calculates each term of the series as 1 / (i * (i - 1)) and adds it to cur.