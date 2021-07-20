function roll(total, idname, step) {
        let n = 0;
        return function () {
            n = (n + step) >= total ? total : (n + step);
            if (n <= total) {
                document.getElementById(idname).innerHTML = n;
            }
        }
}