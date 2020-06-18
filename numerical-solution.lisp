(defconstant THRESH 5e-2)
(defconstant DT 1e-5)
(defconstant SIZE 300)
(defconstant LEN 3)
(defconstant DX (/ 3 SIZE))
(defconstant DY dx)
(defconstant ALPHA 1)
(defconstant F0 (/ (* ALPHA DT) (expt DX 2)))

(defvar *largest* 0)

(defun update-temperature (neighbours previous)
  (let ((temp (+ (* F0 (apply #'+ neighbours)) (* (1+ (* -4 F0)) previous))))
    (when (> (- temp previous) *largest*) (setq *largest* (- temp previous)))
    temp))

(defun get-cell (y x state) (unless (invalidP (* DY y) (* DX x)) (nth x (nth y state))))

(defun get-valid-neighbours (y x state)
  (remove nil (list (get-cell (1+ y) x state) (get-cell (1- y) x state) (get-cell y (1+ x) state) (get-cell y (1- x) state))))

(defun update-cycle (state)
  (loop for i from 0 to SIZE
	collect (loop for j from 0 to SIZE
		      collect (if (border (* DY i) (* DX j)) (get-cell i j state)
				  (unless (invalidp (* DY i) (* DX j)) (update-temperature (get-valid-neighbours i j state) (get-cell i j state)))))))

(defun rangep (num range-min range-max) (and (>= num range-min) (<= num range-max)))

(defun invalidp (y x)
  (or (and (> x 1) (< y 2)) (< x 0) (< y 0) (> x 3) (> y 3)))

(defun border (y x)
  (or (and (= x 0) (<= y 3))
      (and (<= x 1) (= y 0))
      (and (<= x 3) (= y 3))
      (and (= x 1) (<= y 2))
      (and (= x 3) (rangep y 2 3))
      (and (rangep x 1 3) (= y 2))))

(defun thermal-mapping (y x)
  (cond ((and (= x 0) (<= y 3)) 100)
	((and (<= x 1) (= y 0)) 100)
	((and (<= x 3) (= y 3)) 100)
	((and (= x 1) (<= y 2)) 40)
	((and (= x 3) (rangep y 2 3)) 30)
	((and (rangep x 1 3) (= y 2)) 20)
	((invalidp y x) nil)
	(t 0)))

(defun calculation-matrix () (loop for i from 0 to SIZE
				   collect (loop for j from 0 to SIZE
						 collect (thermal-mapping (* DY i) (* DX j)))))

(defun write-to-plot (state)
  (with-open-file (stream "heat_maps/heat_plot.600"
		       :direction :output
		       :if-exists :supersede
		       :if-does-not-exist :create)
  (prin1 state stream)))

(defun solver (&key (state (calculation-matrix)))
  (if (and (<= *largest* THRESH) (/= 0 *largest*)) (write-to-plot state)
      (progn (setq *largest* 0) (solver :state (update-cycle state)))))

(solver)
