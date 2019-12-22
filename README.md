# Santa's Elf Morphing Machine

Solution provided by: [Gianluca Lofrumento](https://github.com/github.io/glofru), [Alessio Di Santo](https://github.com/github.io/alessiobb3b) e [Marco Pinna](https://github.com/github.io/MPinna)

## Problem
Problem in _problem.pdf_ file and a useful information in the challenge description
<img src="img/screenshots/screenshot1.png" />
## Solution

### Find _A<sub>i</sub>_ matrix
First of all we have to find _A<sub>i</sub>_'s eigenvalues.
Given the generic 2x2 matrix <br/>
<img src="img/latex/latex01.gif" style="display: block; margin: 0 auto;" /> <br/>
we know that its characteristic polynomial is
<img src="img/latex/latex02.gif" align="middle"/> <br/>
<img src="img/latex/latex03.gif" /><br/>
<img src="img/latex/latex04.gif" /><br/>
<img src="img/latex/latex05.gif" /><br/>
<img src="img/latex/latex06.gif" /><br/>
<img src="img/latex/latex07.gif" /><br/>

So just with the trace and determinant of _A_ we can find its eigenvalues.

Then from the process of diagonalization of a matrix we know that<br/>
<img src="img/latex/latex08.gif" ><br/>
<img src="img/latex/latex09.gif" /><br/>

If we set <img src="img/latex/latex10.gif"/>, we obtain the similarity transformation:
<img src="img/latex/latex11.gif" /><br/>

where:
 - _M_ is the modal matrix, that is a matrix containing the eigenvectors of A in its columns
 - _D_ is the diagonal matrix of _A_'s eigenvalues, also called 'spectral matrix'

We have everything (clearly we have to invert the modal matrix) so we can easily find the matrix _A_.
### Use the matrix _A<sub>i</sub>_
We know<br/>
<img src="img/latex/latex12.gif" /><br/>

that means <br>
<img src="img/latex/latex13.gif" /><br/>
where x<sub>i</sub> and y<sub>i</sub> are the coordinates in input while x<sub>o</sub> and y<sub>o</sub> are the coordinates in output.

Moreover from the text we know that<br/>
<img src="img/latex/latex14.gif" /><br/>
and that the initial coordinate are (1,3).

We have implemented all this in a python script, after editing a little bit the 'trans.txt' file, as there were some irregularities in the blank spaces that were messing up the `.find()` function in the script (yes, we could have used a regex, but in this case it was way faster to even out the 'trans.txt' file).

The `round()` function at lines 54-55 in the script is needed because of the following reason:
every f<sub>i</sub> transformation applies a linear mapping from <img src="img/latex/latex15.gif" /> to <img src="img/latex/latex15.gif" /> . This, however, does not imply that every A<sub>i</sub> matrix only has natural components. In fact, the matrices belong to <img src="img/latex/latex16.gif" />. <br/>
Since we're dealing with floats, that have a limited precision, approximation errors are always behind the corner. Furthermore, since the output of the i-th iteration is the input of the (i+1)th iteration, we also have to deal with error propagation and amplification.
The `round()` function takes care of all these issues.
You can try and remove it from the script, to have a nice example of what those issues can lead to if they're not properly taken care of.

We computed all the points, plotted them on a scatter plot and got the flag

<img src="img/screenshots/screenshot2.png" /> <br>
<img src="img/screenshots/screenshot3.png" />

