// Index > Header
    var header = document.getElementById('header');
    var navigationHeader = document.getElementById('navigation_header');
    var content = document.getElementById('content')
    var showSidebar = false;

    // Transições de abrir e fechar sidebar
    function toggleSidebar() {
        showSidebar = !showSidebar;
        if (showSidebar){
            navigationHeader.style.marginLeft = '-10vw';
            navigationHeader.style.animationName = 'showSidebar';
            content.style.filter = 'blur(2px)';
        } else {
            navigationHeader.style.marginLeft = '-100vw';
            navigationHeader.style.animationName = '';
            content.style.filter = '';
        }
    }

    // Fechar sidebar se estiver aberta
    function closeSidebar() {
        if (showSidebar) {
            toggleSidebar();
        }
    }

    // Fechar sidebar pelo resize da tela
    window.addEventListener('resize', function(event) {
        if (window.innerWidth > 768 && showSidebar) {
            toggleSidebar();
        }
    });

// Enviar Livro > Genres Select
    document.addEventListener("DOMContentLoaded", function () {
        var selectGenres = document.querySelector("select[name='genres']");
        var selectedGenresSpan = document.getElementById("selectedGenres");
        var clearGenresButton = document.getElementById("clearGenres");

        selectGenres.addEventListener("change", function () {
            var selectedGenres = [];
            var options = this.selectedOptions;
            for (var i = 0; i < options.length; i++) {
                selectedGenres.push(options[i].textContent);
            }
            selectedGenresSpan.textContent = selectedGenres.join(", ");
        });

        clearGenresButton.addEventListener("click", function () {
            selectGenres.querySelectorAll("option").forEach(function(option) {
                option.selected = false;
            });
            selectedGenresSpan.textContent = "";
        });
    });

    //Mostrar filename
    document.getElementById('cover').addEventListener('change', function() {
        const fileName = this.files[0]?.name || 'Nenhum arquivo escolhido';
        document.getElementById('file-name').textContent = fileName;
    });
