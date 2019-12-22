# Santa's Elf Morphing Machine

Solution provided by: [Gianluca Lofrumento](https://github.com/github.io/glofru), [Alessio Di Santo](https://github.com/github.io/alessiobb3b) e [Marco Pinna](https://github.com/github.io/MPinna)

## Problem
Problem in _problem.pdf_ file and a useful information in the challenge description
<img src="img/img_1.jpg" />
## Solution

### Find _A<sub>i</sub>_ matrix
First of all we have to find _A<sub>i</sub>_'s eigenvalues.
Given the generic 2x2 matrix <br/>
<img src="https://latex.codecogs.com/gif.latex?A&space;=&space;\begin{bmatrix}&space;a&space;&&space;b\\&space;c&space;&&space;d&space;\end{bmatrix}" style="display: block; margin: 0 auto;" /> <br/>
we know that its characteristic polynomial is
<img src="https://latex.codecogs.com/gif.latex?det(A&space;-&space;\lambda&space;I)&space;=&space;0" align="middle"/> <br/>
<img src="https://latex.codecogs.com/gif.latex?det(\begin{bmatrix}&space;a-\lambda&space;&&space;b\\&space;c&space;&&space;d-\lambda&space;\end{bmatrix})&space;=&space;0" /><br/>
<img src="https://latex.codecogs.com/gif.latex?(a-\lambda)(d-\lambda)&space;-&space;bc&space;=&space;0" /><br/>
<img src="https://latex.codecogs.com/gif.latex?a&space;d&space;-&space;a\lambda&space;-d\lambda&space;&plus;&space;\lambda&space;^2&space;-&space;bc&space;=&space;0" /><br/>
<img src="https://latex.codecogs.com/gif.latex?\lambda&space;^2&space;-(a&plus;d)\lambda&space;&plus;&space;ad&space;-&space;bc&space;=&space;0" /><br/>
<img src="https://latex.codecogs.com/gif.latex?\lambda&space;^2&space;-Tr(a)\lambda&space;&plus;&space;det(A)&space;=&space;0" /><br/>

So just with the trace and determinant of _A_ we can find its eigenvalues.
Then from the process of diagonalization of a matrix we know that<br/>
<img src="https://latex.codecogs.com/gif.latex?A&space;=&space;LJR" ><br/>
<img src="https://latex.codecogs.com/gif.latex?A&space;=&space;R^{-1}JR" /><br/>
where:
 - _R_ is the modal matrix, that is a matrix containing the eigenvectors of A in its columns
 - _J_ is the diagonal matrix of _A_'s eigenvalues

We have everything (clearly we have to invert the modal matrix) so we can easily find the matrix _A_.
### Use the matrix _A<sub>i</sub>_
We know<br/>
<img src="https://latex.codecogs.com/gif.latex?f_i&space;:&space;N^2&space;\rightarrow&space;N^2"/><br/>
that means
<img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;A_i&space;\end{bmatrix}&space;\begin{bmatrix}&space;x_i\\&space;y_i&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;x_o\\&space;y_o&space;\end{bmatrix}" /><br/>
where x<sub>i</sub> and y<sub>i</sub> are the coordinates in input while x<sub>o</sub> and y<sub>o</sub> are the coordinates in output.

Moreover from the text we know that<br/>
<img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;A_i&space;\end{bmatrix}&space;\begin{bmatrix}&space;x_{i-1}\\&space;y_{i-1}&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;x_i\\&space;y_i&space;\end{bmatrix}&space;\quad\quad\quad&space;\forall&space;i&space;\in&space;[1,&space;n]" /><br/>
and that the initial coordinate are (1,3). 
We have just implemented all this in a python program and that was the result:<br/>
<img src="img/img_2.jpg" /><br/>
<img src="img/img_3.jpg" />

