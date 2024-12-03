fn main() {
    let precision: u32 = 1000000000;
    let mut a: f64 = 0.0;
    let mut b: f64 = 2.0;
    for _ in 0..precision {
        a = (2.0 + a).sqrt();
        b = (2.0 * b) / a;
    }
    println!("pi = {}", b);
}