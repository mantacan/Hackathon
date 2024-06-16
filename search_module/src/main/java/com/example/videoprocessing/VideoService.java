package com.example.videoprocessing;

import lombok.RequiredArgsConstructor;
import org.elasticsearch.client.RestHighLevelClient;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.data.elasticsearch.core.ElasticsearchOperations;
import org.springframework.data.elasticsearch.core.IndexOperations;
import org.springframework.data.elasticsearch.core.mapping.IndexCoordinates;
import org.springframework.data.elasticsearch.core.query.IndexQuery;
import org.springframework.data.elasticsearch.core.query.IndexQueryBuilder;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;

import java.util.Map;

@Service
@RequiredArgsConstructor
public class VideoService {


    @Autowired
    private RestHighLevelClient esClient;
    @Autowired
    private WebClient webClient;

    private final ElasticsearchOperations elasticsearchOperations;


    public void indexData(Map<String, Object> jsonData) {
        IndexQuery indexQuery = new IndexQueryBuilder()
                .withObject(jsonData)
                .build();

        IndexOperations indexOperations = elasticsearchOperations.indexOps(IndexCoordinates.of("new_index"));
        if (!indexOperations.exists()) {
            indexOperations.create();
        }

        elasticsearchOperations.index(indexQuery, IndexCoordinates.of("new_index"));
    }
}
