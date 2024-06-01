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
