function start(index, idname, step, runtime = 1000){
    let rolling = roll(index, idname, step);
    runtime = (runtime >= 300) ? runtime : 1000;
    for (let i = 0; i < (index/step); i++) {
        let timer = setTimeout(rolling, (runtime/index)*i*step);
    }
    clearTimeout(timer);
}