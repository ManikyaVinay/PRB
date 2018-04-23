node{
    def gitUrl = 'https://api.github.com/repos/ManikyaVinay/PRB/commits'

    // Reading projects from GitLab REST API
    def projectList = new URL("${gitUrl}")
    def projects = new groovy.json.JsonSlurper().parse(projectList.newReader())
    println "lasst commit: ${projects[0].sha}"
    projects.each {
      println it.sha
    }
}
