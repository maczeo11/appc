fn recc(mut vec: Vec<i32>) {
    if vec.len() <= 1 {
        println!("Base case: {:?}", vec);
        return;
    }

    let mid = vec.len() / 2;

    // Drain the left half
    let left = vec.drain(..mid).collect::<Vec<i32>>();
    let right = vec; // vec now holds the right half

    println!("Splitting: Left = {:?}, Right = {:?}", left, right);

    // Recursive calls
    recc(left);
    recc(right);
}

fn main() {
    let vec = vec![544, 6556, 44, 44, 5454, 544, 33, 454];
    recc(vec);
}