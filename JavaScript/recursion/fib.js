function fib(n) {
    if (n <= 1){
        return n
    }
    return fib(n-1) + fib(n-2);
}

function fib_memo(n, memo={}){
    // console.log(n, memo)
    if(n in memo){
        return memo[n];
    }
    if (n <= 1){
        return n
    }
    const return_val = fib_memo(n-1, memo) + fib_memo(n-2, memo);
    memo[n] = return_val
    return return_val;
}

function fib_memo(n, memo={}){
    // console.log(n, memo)
    if(n in memo){
        return memo[n];
    }
    if (n <= 1){
        return n
    }
    const return_val = fib_memo(n-1, memo) + fib_memo(n-2, memo);
    memo[n] = return_val
    return return_val;
}

let fib_store={};
const get = (n) => fib_store[n]
const set = (n, v) => fib_store[n] = v


function fib_memo_g(n){
    if (n <= 1){
        return n
    }
    const return_val = (
        get(n - 1) || fib_memo_g(n - 1) + 
        get(n - 2) || fib_memo_g(n - 2)
    );

    set(n, return_val)
    return return_val;
}

console.log(">==========|Testing Standard method|==========<")
console.log("fig 10");
console.log(fib(10));
for (let i = 0; i <= 10; i++){
    console.log(i, fib(i))
}

console.log(">==========|Testing Memo method|===========<")

let tests = [10, 100, 1000, 10000, 100000];
for (const test of tests) {
    try {
        const test_str = `fib ${test} memo`
        console.log(test_str);
        console.time(test_str);
        console.log(fib_memo(test))
        console.timeEnd(test_str)
    }catch(e){
        // note the stack size error
        // console.log(e);
        console.log("RangeError: Maximum call stack size exceeded");
    }
}


console.log(">==========|Testing Memo (Global storage) method|===========<")
for (const test of tests) {
    try {
        const test_str = `fib ${test} memo g`
        console.log(test_str);
        console.time(test_str);
        console.log(fib_memo_g(test))
        console.timeEnd(test_str)
    }catch(e){
        // note the stack size error
        // console.log(e);
        console.log("RangeError: Maximum call stack size exceeded");
    }
}


/*
    note that here, we still go over the stack. 
    but what if we go in smaller increments 
*/

console.log(">==========|Testing Memo (Global storage) smaller batches method|===========<")

fib_store = {}; // reset store
tests = [10, 100, 1000, 5000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
for (const test of tests) {
    try {
        const test_str = `fib ${test} memo g`
        console.log(test_str);
        console.time(test_str);
        console.log(fib_memo_g(test))
        console.timeEnd(test_str)
    }catch(e){
        // note the stack size error
        // console.log(e);
        console.log("RangeError: Maximum call stack size exceeded");
    }
}

/* 
    Note that this problem will completely goes away if we would use tabulation
    more on that later
*/ 
