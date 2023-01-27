use pyo3::prelude::*;
use rand::{thread_rng, Rng};

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn gen_rand_vals() -> PyResult<[f64; 1000]> {
    let mut rng = thread_rng();
    let rand_vals: [f64; 1000] = core::array::from_fn(|_| rng.gen());
    Ok(rand_vals)
}


#[pyfunction]
fn gen_pi(NT: i32) -> PyResult<f32> {
    let mut rng = thread_rng();
    let mut Nc = 0;
    
    for _ in 1..NT {
        let x: f32 = rng.gen_range(-1.0..1.0);
        let y: f32 = rng.gen_range(-1.0..1.0);
        if (x*x + y*y).sqrt() <= 1_f32 {
            Nc += 1
        }
    }

    Ok(4_f32 * Nc as f32 / NT as f32)
}


/// A Python module implemented in Rust.
#[pymodule]
fn MC_sim(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(gen_rand_vals, m)?)?;
    m.add_function(wrap_pyfunction!(gen_pi, m)?)?;
    Ok(())
}
