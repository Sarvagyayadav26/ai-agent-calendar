navigator.mediaDevices.getUserMedia({ audio: true })
  .then(stream => {
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    let chunks = [];
    mediaRecorder.ondataavailable = e => chunks.push(e.data);

mediaRecorder.onstop = async () => {
    status.textContent = 'Processing audio...';
    let blob = new Blob(chunks, { type: 'audio/wav' });
    chunks = [];

    // Play back the recorded audio immediately for confirmation
    let audioUrl = URL.createObjectURL(blob);
    let audio = new Audio(audioUrl);
    audio.play();
    
    audio.onplay = () => {
        status.textContent = 'Playing back your recording...';
    };
    audio.onended = () => {
        status.textContent = 'Playback finished.';
    };
    audio.onerror = (e) => {
        status.textContent = 'Error playing back audio';
        console.error('Audio playback error', e);
    };

    // If you want to keep the backend call for later, you can leave the fetch code below, but it is not needed for this purpose.
};

