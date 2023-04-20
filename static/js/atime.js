 const nodes = []
    function add() {
      const tpl = document.querySelector('template')
      const item = tpl.content.children[0]
      const timeline = document.querySelector('.timeline')
      nodes.forEach(it => it.classList.remove('current'))
      const node = item.cloneNode(true)
      node.classList.add('current')
      nodes.push(node)
      console.log(node, node.classList)
      timeline.appendChild(node)
      node.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' })
    }

