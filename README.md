# 107transfer

Polynomials for optimizing electronic component transfer functions.

Project for semester 2 of the Epitech Math module.

### Description

The transfer function of an electronic component is a rational function, composed of polynomials in the numerator and denominator, that computes the frequency response. This program calculates the combined transfer function for several components in cascade, and prints the frequency response for input values ranging from 0 to 1 with a step of 0.001.

The program:
1. Accepts the numerator and denominator polynomials of each component as input.
2. Multiplies the transfer functions of all components in cascade.
3. Outputs the frequency response values for each input frequency in the given range.

## Getting Started

### Dependencies

- [Python3](https://python.org/)

### Installation

* Download/Clone the repository and enter its directory.
* Now you are ready to run the code.

## Usage

**Execution:** ```./107transfer [num den]+```

### Arguments
- **`num`**: Polynomial numerator defined by its coefficients, split by `*`.
- **`den`**: Polynomial denominator defined by its coefficients, split by `*`.

### Examples

To compute the transfer function for a polynomial:

```
$> ./107transfer "0*1*2*3*4" "1"
$> ./107transfer "0*0*9" "1*3*5" "2*4*6" "8*8*8"
```

## Acknowledgments

* [Epitech](https://www.epitech.eu/)

## Authors

* **Daniel Sanchez** ([GitHub](https://github.com/angsanch) / [LinkedIn](https://www.linkedin.com/in/angeldanielsanchez/))
* **Xinru Xu** ([GitHub](https://github.com/Exinru) / [LinkedIn](https://www.linkedin.com/in/xinru-xu/))

## License

This project is licensed under the GNU Public License version 3.0 - see the [LICENSE](LICENSE) file for details.
