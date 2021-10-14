import React, { Component } from "react";
import axiosInstance from "../axiosApi";

class Hello extends Component {
    constructor(props) {
        super(props);
        this.state = {
           articles :[],
        };

        this.getMessage = this.getArticles.bind(this)
    }
/* 
    getArticles(){
        
            axiosInstance.get('/api/articles/')
            .then((resp) => {
                console.log(resp.data)
                this.setState({
                    articles: resp.data,
                });
                return articles;
            })
           .catch(error => {
            console.log("Error: ", JSON.stringify(error, null, 4));
            throw error;
        }
        )
    } */
  getArticles(){
        axiosInstance.get('/api/articles/')
            .then((resp) => {
                console.log(resp.data)
                this.setState({
                    articles: resp.data,
                });
                return articles;
            })
           .catch(error => {
            console.log("Error: ", JSON.stringify(error, null, 4));
            throw error;
        }
        )
    }

    componentDidMount(){
       
        const articles = this.getArticles();
        console.log("articles: ", JSON.stringify(articles, null, 4));
    }

    render(){
        return (
            <div>
                {this.state.articles.map(article => {
                    return (
                        <h3 key={article.id}>{article.title}</h3>
                    )
                })}
            </div>
        )
    }
}

export default Hello;