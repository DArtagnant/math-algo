
fn divisors(n:u64) -> Vec<u64> {
    assert!(n != 0);
    let mut r: Vec<u64> = Vec::new();
    for t in 1..=((n as f64).sqrt().floor() as u64) {
        if n % t == 0 {
            r.push(t);
            let d = (n / t) as u64;
            if d != t {
                r.push(d);   
            }
        }
    }
    r
}

fn is_perfect(n: u64) -> bool {
    divisors(n).iter().sum::<u64>() == 2*n
}

fn perfects(max: u64) -> Vec<u64> {
    let mut r: Vec<u64> = Vec::new();
    for n in 1..=max {
        if is_perfect(n) {
            r.push(n);
        }
    }
    r
}

fn main() {
    println!("div 6 : {:?}", divisors(6));
    println!("div 1024 : {:?}", divisors(1024));
    println!("perfect 6 : {:?}", is_perfect(6));
    println!("perfect 10 : {:?}", is_perfect(10));
    println!("perfects 1000000 : {:?}", perfects(1000000));
}