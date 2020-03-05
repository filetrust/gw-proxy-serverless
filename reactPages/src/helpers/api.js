import axios from "axios";

/**
 * Fetch data from given url
 * @param {*} url
 * @param {*} options
 */
export const fetchJSON = (url, options = {}) => {
    return fetch(url, options)
        .then(response => {
            if (!response.status === 200) {
                throw response.json();
            }
            return response.json();
        })
        .then(json => {
            return json;
        })
        .catch(error => {
            throw error;
        });
};

export const client = (token = null) => {
    const defaultOptions = {
      headers: token
        ? {
            Authorization: `Bearer ${token}`
          }
        : {}
    };
  
    return {
      get: (url, options = {}) =>
        axios.get(url, { ...defaultOptions, ...options }),
      post: (url, data, options = {}) =>
        axios.post(url, data, { ...defaultOptions, ...options }),
      put: (url, data, options = {}) =>
        axios.put(url, data, { ...defaultOptions, ...options }),
      delete: (url, options = {}) =>
        axios.delete(url, { ...defaultOptions, ...options })
    };
  };