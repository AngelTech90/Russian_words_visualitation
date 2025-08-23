function showPopup(englishWord, russianWord, englishSentence, russianSentence) {
            document.getElementById('popup-english-word').textContent = englishWord;
            document.getElementById('popup-russian-word').textContent = russianWord;
            document.getElementById('popup-english-sentence').textContent = englishSentence;
            document.getElementById('popup-russian-sentence').textContent = russianSentence;
            
            document.getElementById('popup-overlay').classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closePopup() {
            document.getElementById('popup-overlay').classList.remove('active');
            document.body.style.overflow = 'auto';
        }

        // Close popup with Escape key
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') {
                closePopup();
            }
        });
